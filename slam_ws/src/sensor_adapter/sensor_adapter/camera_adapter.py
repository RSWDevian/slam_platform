import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class CameraAdapter(Node):
    def __init__(self):
        super().__init__('camera_adapter')

        self.publisher = self.create_publisher(
            Image,
            "/slam/camera/image_raw",
            10
        )

        self.subscription = self.create_subscription(
            Image,
            "/camera/image_raw",
            self.callback,
            10
        )

    def callback(self, msg):
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CameraAdapter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()