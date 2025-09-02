import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PLCSender(Node):
    def __init__(self):
        super().__init__('PLC_Control') # Node name

        # Create publisher: topic_name, message_type, queue_size
        self.publisher_ = self.create_publisher(String, 'status_updates',10)
        self.subscription = self.create_subscription(String, 'hmi/unified_status', self.listener_callback, 10)

        # Timer to publish every 0.5 seconds
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.print = ""

    def listener_callback(self, msg):
        self.get_logger().info(f' I heard: {msg.data}')
        self.print = String()
        self.print.data = msg.data

    def timer_callback(self):
        msg = String()
        msg.data = f'Tim Apple spotted doing pineapple dance in aisle {self.i}!'
        self.publisher_.publish(self.print)
        self.get_logger().info(f'Publishing: "{self.print.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args) # Initialize ROS2
    pineapple_gossip_bot = PLCSender()
    rclpy.spin(pineapple_gossip_bot) # Keep node running
    pineapple_gossip_bot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()