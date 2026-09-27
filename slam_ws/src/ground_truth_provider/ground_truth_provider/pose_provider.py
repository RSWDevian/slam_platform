import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from tf2_ros import (
    Buffer,
    ConnectivityException,
    ExtrapolationException,
    LookupException,
    TransformListener,
)

class PoseProvider(Node):
    def __init__(self):
        super().__init__('ground_truth_pose_provider')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.publisher = self.create_publisher(PoseStamped, '/ground_truth/pose', 10)
        # Set a timer to publish the pose at a regular interval
        self.timer = self.create_timer(0.1, self.publish_pose)  # Publish at 10 Hz

    def publish_pose(self):
        try:
            transform = self.tf_buffer.lookup_transform(
                "odom",
                "base_link",
                rclpy.time.Time()
            )

            msg = PoseStamped()
            msg.header = transform.header
            msg.pose.position.x = transform.transform.translation.x
            msg.pose.position.y = transform.transform.translation.y
            msg.pose.position.z = transform.transform.translation.z
            msg.pose.orientation = transform.transform.rotation

            self.publisher.publish(msg)

        except (LookupException, ConnectivityException, ExtrapolationException) as e:
            self.get_logger().warn(
                f"Could not look up odom -> base_link transform: {e}",
                throttle_duration_sec=5.0,
            )

def main(args=None):
    rclpy.init(args=args)
    node = PoseProvider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
