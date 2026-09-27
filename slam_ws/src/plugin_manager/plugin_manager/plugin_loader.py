"""Dynamically imports and instantiates SLAM plugins declared in a PluginRegistry."""
import importlib
from typing import Optional, Tuple

from plugin_manager.plugin_registry import PluginDeclaration
from plugin_manager.plugin_status import PluginState, PluginStatus


class PluginLoader:
    """Resolves a PluginDeclaration into a live plugin instance."""

    def load(self, declaration: PluginDeclaration) -> Tuple[Optional[object], PluginState]:
        state = PluginState(plugin_id=declaration.plugin_id, status=PluginStatus.LOADING)

        try:
            module = importlib.import_module(declaration.module_path)
        except ImportError as exc:
            state.status = PluginStatus.NOT_IMPLEMENTED
            state.message = f"Module '{declaration.module_path}' is not importable: {exc}"
            return None, state
        except Exception as exc:  # module exists but errors while importing
            state.status = PluginStatus.LOAD_ERROR
            state.message = f"Error importing '{declaration.module_path}': {exc}"
            return None, state

        plugin_class = getattr(module, declaration.class_name, None)
        if plugin_class is None:
            state.status = PluginStatus.NOT_IMPLEMENTED
            state.message = (
                f"Class '{declaration.class_name}' not found in '{declaration.module_path}'"
            )
            return None, state

        try:
            instance = plugin_class()
        except TypeError as exc:
            # Raised when an ABC subclass leaves abstract methods unimplemented.
            state.status = PluginStatus.NOT_IMPLEMENTED
            state.message = f"'{declaration.class_name}' cannot be instantiated: {exc}"
            return None, state
        except Exception as exc:
            state.status = PluginStatus.LOAD_ERROR
            state.message = f"Unexpected error instantiating '{declaration.class_name}': {exc}"
            return None, state

        state.status = PluginStatus.LOADED
        state.message = "Loaded successfully"
        return instance, state
