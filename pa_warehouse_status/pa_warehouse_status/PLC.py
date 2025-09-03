import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
from datetime import datetime
import pytz

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

    def convTime(self, time) -> str:
        utc_tz = pytz.utc
        aest_tz = pytz.timezone('Australia/Sydney')
        now_utc = datetime.now(utc_tz)
        now_aest = now_utc.astimezone(aest_tz)
        return (now_aest - now_utc).total_seconds()

    def listener_callback(self, msg):
        try:
            self.get_logger().info(f' I heard: {msg.data}')
            self.print = String()
            # Convert message to json datatype for phrasing
            jsonData = json.loads(msg.data)
            self.timestamp = str(self.convTime(jsonData['stamp']['sec']))
            self.boxWeight = str(jsonData['box']['weight_raw'])
            self.boxLocation = str(jsonData['box']['location'])
            self.countBig = str(jsonData['counts']['big'])
            self.countMed = str(jsonData['counts']['medium'])
            self.countSml = str(jsonData['counts']['small'])
            self.countTot = str(jsonData['counts']['total'])
            self.print.data = "Time: " + self.timestamp + "\nW: " + self.boxWeight + "\nL: " + self.boxLocation + "\nB: " + self.countBig + "\nM: " +self.countMed + "\nS: " +self.countSml + "\nT: " +self.countTot
        except json.JSONDecodeError:
            self.get_logger().error("Failed to phrase JSON")

    def timer_callback(self):
        msg = String()
        msg.data = f'Tim Apple spotted doing pineapple dance in aisle {self.i}!'
        self.publisher_.publish(self.print)
        self.get_logger().info(f'Publishing: \n"{self.print.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args) # Initialize ROS2
    pineapple_gossip_bot = PLCSender()
    rclpy.spin(pineapple_gossip_bot) # Keep node running
    pineapple_gossip_bot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()