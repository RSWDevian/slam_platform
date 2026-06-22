import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path

class PathProvider(Node):
    def __init__(self):
        super().__init__('ground_truth_path_provider')
        self.path = Path()

        self.publisher = self.create_publisher(
            Path,
            '/ground_truth/path',
            10
        )

        self.subscription = self.create_subscription(
            Path,
            '/ground_truth/pose',
            self.callback,
            10
        )


    def callback(self, msg):
        self.path.header = msg.header
        self.path.poses.append(msg)
        self.publisher.publish(self.path)

def main(args=None):
    rclpy.init(args=args)
    node = PathProvider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
