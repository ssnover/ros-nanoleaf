import rclpy as ros
from rclpy.node import Node
from std_msgs.msg import Bool
from nanoleaf import Aurora


class AuroraSubscriber(Node):
    def __init__(self):
        super().__init__('aurora')
        self.subscription = self.create_subscription(
            Bool,
            'onoff',
            self.listener_callback,
            10)
        self.subscription
        self.aurora = Aurora("192.168.1.12", "55AcCZriAkQuoehjzWTyQSY8dxPgS9dM")

    def listener_callback(self, msg):
        self.get_logger().info('Changing Nanoleaf Aurora on/off state: {}'.format(msg.data))
        self.aurora.on = bool(msg.data)


def main(args=None):
    ros.init(args=args)
    aurora = AuroraSubscriber()
    ros.spin(aurora)
    aurora.destroy_node()
    ros.shutdown()


if __name__ == "__main__":
    main()

