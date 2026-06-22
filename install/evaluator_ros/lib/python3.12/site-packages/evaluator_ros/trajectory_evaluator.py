import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Float64   

class TrajectoryEvaluator(Node):
    def __init__(self):
        super().__init__("trajectory_evaluator")
        self.gt_trajectory = []
        self.slam_trajectory = []

        self.gt_sub = self.create_subscription(
            PoseStamped,
            "/ground_truth/pose",
            self.gt_callback,
            10
        )

        self.slam_sub = self.create_subscription(
            PoseStamped,
            "/slam_output/pose",
            self.slam_callback,
            10
        )

        self.ate_pub = self.create_publisher(
            Float64,
            "/evaluation/ate",
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.compute_ate
        )

    def gt_callback(self, msg):
        self.gt_trajectory.append(
            [
                msg.pose.position.x,
                msg.pose.position.y,
                msg.pose.position.z
            ]
        )

    def slam_callback(self, msg):
        self.slam_trajectory.append(
            [
                msg.pose.position.x,
                msg.pose.position.y,
                msg.pose.position.z
            ]
        )

    def compute_ate(self):
        n = min(
            len(self.gt_trajectory),
            len(self.slam_trajectory)
        )

        if n<2:
            return
        
        squared_error_sum = 0.0
        
        for i in range(n):
            gt = self.gt_trajectory[i]
            slam = self.slam_trajectory[i]

            dx = gt[0] - slam[0]
            dy = gt[1] - slam[1]
            dz = gt[2] - slam[2]

            squared_error_sum += dx*dx + dy*dy + dz*dz
            ate = math.sqrt(squared_error_sum/n)
            msg = Float64()
            msg.data = ate
            self.ate_pub.publish(msg)
            self.get_logger().info(f"ATE: {ate:.4f}")

def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryEvaluator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

    