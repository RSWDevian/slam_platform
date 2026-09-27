import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class OdomAdapter(Node):
    def __init__(self):
        super().__init__('odom_adapter')

        self.publisher = self.create_publisher(
            Odometry,
            "/slam/odom",
            10
        )

        self.subscription = self.create_subscription(
            Odometry,
            "/odom",
            self.callback,
            10
        )

    def callback(self, msg):
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = OdomAdapter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()