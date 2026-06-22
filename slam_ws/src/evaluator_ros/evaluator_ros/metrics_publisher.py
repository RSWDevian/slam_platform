import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from std_msgs.msg import Int32
from slam_interfaces.msg import SLAMMetrics

class MetricsPublisher(Node):

    def __init__(self):

        super().__init__('metrics_publisher')
        self.metrics = SLAMMetrics()

        #? Subscribtions
        #& Trajectory Evaluator Metrics
        self.create_subscription(
            Float64,
            "/evaluation/ate",
            self.ate_callback,
            10
        )

        # self.create_subscription(
        #     Float64,
        #     "/evaluation/rpe",
        #     self.rpe_callback,
        #     10
        # )

        # self.create_subscription(
        #     Float64,
        #     "/evaluation/drift",
        #     self.drift_callback,
        #     10
        # )

        #& Resource Monitor Metrics
        self.create_subscription(
            Float64,
            "/evaluation/cpu_usage",
            self.cpu_usage_callback,
            10
        )

        self.create_subscription(
            Float64,
            "/evaluation/memory_usage",
            self.memory_callback,
            10
        )

        self.create_subscription(
            Float64,
            "/evaluation/runtime",
            self.runtime_callback,
            10
        )

        self.create_subscription(
            Int32,
            "/evaluation/num_threads",
            self.num_threads_callback,
            10
        )

        #? Publishers
        self.metrics_pub = self.create_publisher(
            SLAMMetrics,
            "/evaluation/metrics",
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_metrics
        )

        self.get_logger().info(
            "Metrics Publisher Started. Publishing metrics to /evaluation/metrics topic."
        )
    
    #~ Trajectory Evaluator Metrics Callbacks
    def ate_callback(self, msg):
        self.metrics.ate = msg.data

    def rpe_callback(self, msg):
        self.metrics.rpe = msg.data

    def drift_callback(self, msg):
        self.metrics.drift = msg.data

    #~ Resource Monitor Metrics Callbacks
    def cpu_usage_callback(self, msg):
        self.metrics.cpu_usage = msg.data

    def memory_callback(self, msg):
        self.metrics.memory_usage = msg.data

    def runtime_callback(self, msg):
        self.metrics.runtime = msg.data

    def num_threads_callback(self, msg):
        self.metrics.num_threads = msg.data

    #~ Publish Metrics
    def publish_metrics(self):
        self.metrics_pub.publish(
            self.metrics
        )

def main(args=None):
    rclpy.init(args=args)
    node = MetricsPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()    

if __name__ == "__main__":
    main()