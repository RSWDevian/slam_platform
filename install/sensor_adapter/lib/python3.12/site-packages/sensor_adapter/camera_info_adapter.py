import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class CameraInfoAdapter(Node):
    def __init__(self):
        super().__init__('camera_info_adapter')

        self.publisher = self.create_publisher(
            Image,
            "/slam/camera/camera_info",
            10
        )

        self.subscription = self.create_subscription(
            Image,
            "/camera/camera_info",
            self.callback,
            10
        )

    def callback(self, msg):
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CameraInfoAdapter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()