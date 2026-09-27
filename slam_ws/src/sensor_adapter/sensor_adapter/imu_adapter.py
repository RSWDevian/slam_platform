import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

class ImuAdapter(Node):
    def __init__(self):
        super().__init__('imu_adapter')

        self.publisher = self.create_publisher(
            Imu,
            "/slam/imu/data",
            10
        )

        self.subscription = self.create_subscription(
            Imu,
            "/imu/data",
            self.callback,
            10
        )

    def callback(self, msg):
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ImuAdapter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()