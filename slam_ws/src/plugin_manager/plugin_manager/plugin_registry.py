"""Loads the declarations of installable SLAM plugins from a YAML config."""
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

import yaml


@dataclass
class PluginDeclaration:
    plugin_id: str
    package: str
    module: str
    class_name: str
    description: str = ""

    @property
    def module_path(self) -> str:
        return f"{self.package}.{self.module}" if self.module else self.package


class PluginRegistry:
    """Holds the set of plugins declared in a plugins.yaml config file."""

    def __init__(self):
        self._plugins: Dict[str, PluginDeclaration] = {}

    @classmethod
    def from_yaml(cls, config_path: str) -> "PluginRegistry":
        registry = cls()
        path = Path(config_path)
        if not path.is_file():
            raise FileNotFoundError(f"Plugin registry config not found: {config_path}")

        with path.open("r") as f:
            data = yaml.safe_load(f) or {}

        for entry in data.get("plugins", []):
            registry.register(
                PluginDeclaration(
                    plugin_id=entry["id"],
                    package=entry["package"],
                    module=entry.get("module", ""),
                    class_name=entry["class"],
                    description=entry.get("description", ""),
                )
            )
        return registry

    def register(self, declaration: PluginDeclaration) -> None:
        self._plugins[declaration.plugin_id] = declaration

    def get(self, plugin_id: str) -> Optional[PluginDeclaration]:
        return self._plugins.get(plugin_id)

    def list_ids(self) -> List[str]:
        return list(self._plugins.keys())

    def all(self) -> List[PluginDeclaration]:
        return list(self._plugins.values())
