import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LidarAdapter(Node):
    def __init__(self):
        super().__init__('lidar_adapter')

        self.publisher = self.create_publisher(
            LaserScan,
            "/slam/lidar/scan",
            10
        )

        self.subscription = self.create_subscription(
            LaserScan,
            "/scan",
            self.callback,
            10
        )

    def callback(self, msg):
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = LidarAdapter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()