import time
import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from std_msgs.msg import Int32

class ResourceMonitor(Node):
    def __init__(self):
        super().__init__("resource_monitor")
        self.start_time = time.time()
        self.process = psutil.Process()

        self.cpu_pub = self.create_publisher(
            Float64,
            "/evaluation/cpu_usage",
            10
        )

        self.runtime_pub = self.create_publisher(
            Float64,
            "/evaluation/runtime",
            10
        )

        self.thread_pub = self.create_publisher(
            Int32,
            "/evaluation/num_threads",
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_metrics
        )

    def publish_metrics(self):
        cpu = Float64()
        cpu.data = self.process.cpu_percent()
        self.cpu_pub.publish(cpu)

        memory = Float64()
        memory.data = self.process.memory_info().rss/(1024*1024)
        self.memory_pub.publish(memory)

        runtime = Float64()
        runtime.data = time.time() - self.start_time
        self.runtime_pub.publish(runtime)

        threads = Int32()
        threads.data = self.process.num_threads()
        self.thread_pub.publish(threads)

def main(args=None):
    rclpy.init(args=args)
    node = ResourceMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()