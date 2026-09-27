import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Float64

class PoseComparator(Node):
    def __init__(self):
        super().__init__("pose_comparator")
        self.gt_pose = None
        self.slam_pose = None

        self.gt_pose_sub = self.create_subscription(
            PoseStamped,
            "/ground_truth/pose",
            self.gt_callback,
            10
        )

        self.slam_pose_sub = self.create_subscription(
            PoseStamped,
            "/slam_output/pose",
            self.slam_callback,
            10
        )

        self.position_error_pub = self.create_publisher(
            Float64,
            "/evaluation/position_error",
            10
        )

        self.orientation_error_pub = self.create_publisher(
            Float64,
            "/evaluation/orientation_error",
            10
        )

        self.timer = self.create_timer(
            0.05,
            self.compare_poses
        )

    def gt_callback(self, msg):
        self.gt_pose = msg

    def slam_callback(self, msg):
        self.slam_pose = msg

    def compare_poses(self):
        if self.gt_pose is None:
            return
        if self.slam_pose is None:
            return
        
        self.compute_position_error()
        self.compute_orientation_error()
        
        
    def compute_position_error(self):
        dx = self.gt_pose.pose.position.x - self.slam_pose.pose.position.x
        dy = self.gt_pose.pose.position.y - self.slam_pose.pose.position.y
        dz = self.gt_pose.pose.position.z - self.slam_pose.pose.position.z
        error = math.sqrt(dx*dx + dy*dy + dz*dz)
        msg = Float64()
        msg.data = error
        self.position_error_pub.publish(msg)
    
    def compute_orientation_error(self):
        gt_q = self.gt_pose.pose.orientation
        slam_q = self.slam_pose.pose.orientation

        dot = gt_q.x * slam_q.x + gt_q.y * slam_q.y + gt_q.z * slam_q.z + gt_q.w * slam_q.w
        angle = 2 * math.acos(abs(dot))
        msg = Float64()
        msg.data = angle
        self.orientation_error_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = PoseComparator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()