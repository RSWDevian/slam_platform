"""
Abstract class for all slam plugins.
"""
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Path

class SlamPlugin(ABC):
    """
    Abstract base class that defines the interface of all slam plugins.
    Each SLAM algorithm must inherit from this class.
    """
    def __init__(self):
        self.node: Optional[Node] = None
        self.plugin_name: str = ""
        self.initialized: bool = False
        self.status: str = "UnInitialized"
        self.config: Dict[str, Any] = {}

    @abstractmethod
    def initialize(self, node: Node, config_path: str) -> bool:
        pass

    @abstractmethod
    def process_image(self, image_msg, timestamp: float) -> None:
        pass

    @abstractmethod
    def process_imu(self, imu_msg, timestamp: float) -> None:
        pass

    @abstractmethod
    def get_current_pose(self) -> Optional[PoseWithCovarianceStamped]:
        pass

    @abstractmethod
    def get_trajectory(self) -> Optional[Path]:
        pass

    @abstractmethod
    def get_status(self) -> str:
        pass

    @abstractmethod
    def shutdown(self) -> None:
        pass

    @abstractmethod
    def configure(self, config: Dict[str, Any]) -> bool:
        pass

    def get_plugin_info(self) -> Dict[str, Any]:
        return {
            "name": self.plugin_name,
            "initialized": self.initialized,
            "status": self.status,
            "config": self.config
        }
