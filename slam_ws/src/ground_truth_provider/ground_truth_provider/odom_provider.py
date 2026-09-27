import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from tf2_ros import (
    Buffer,
    ConnectivityException,
    ExtrapolationException,
    LookupException,
    TransformListener,
)

class OdomProvider(Node):
    def __init__(self):
        super().__init__('ground_truth_odom_provider')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.publisher = self.create_publisher(Odometry, '/ground_truth/odom', 10)
        # Set a timer to publish odometry at a regular interval
        self.timer = self.create_timer(0.1, self.publish_odom)  # Publish at 10 Hz

    def publish_odom(self):
        try:
            transform = self.tf_buffer.lookup_transform(
                "odom",
                "base_link",
                rclpy.time.Time()
            )

            msg = Odometry()
            msg.header = transform.header
            msg.child_frame_id = "base_link"
            msg.pose.pose.position.x = transform.transform.translation.x
            msg.pose.pose.position.y = transform.transform.translation.y
            msg.pose.pose.position.z = transform.transform.translation.z
            msg.pose.pose.orientation = transform.transform.rotation

            self.publisher.publish(msg)

        except (LookupException, ConnectivityException, ExtrapolationException) as e:
            self.get_logger().warn(
                f"Could not look up odom -> base_link transform: {e}",
                throttle_duration_sec=5.0,
            )

def main(args=None):
    rclpy.init(args=args)
    node = OdomProvider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
