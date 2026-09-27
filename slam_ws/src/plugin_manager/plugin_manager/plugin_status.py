"""Status tracking primitives for SLAM plugins managed by plugin_manager."""
from dataclasses import dataclass, field
from enum import Enum


class PluginStatus(Enum):
    REGISTERED = "registered"
    LOADING = "loading"
    LOADED = "loaded"
    NOT_IMPLEMENTED = "not_implemented"
    LOAD_ERROR = "load_error"


@dataclass
class PluginState:
    plugin_id: str
    status: PluginStatus = PluginStatus.REGISTERED
    message: str = ""

    def to_dict(self) -> dict:
        return {
            "plugin_id": self.plugin_id,
            "status": self.status.value,
            "message": self.message,
        }
