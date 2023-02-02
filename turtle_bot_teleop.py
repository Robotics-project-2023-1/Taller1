import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class Turtle_bot_teleop(Node):

    def __init__(self):
        super().__init__('turtle_bot_teleop')
        self.publisher_ = self.create_publisher(Twist, 'turtlebot_cmdVel', 10)  # no se que poner en tamano de la fila 20
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.linear.y = 2.0
        msg.linear.z = 2.0
        msg.angular.x = 2.0
        msg.angular.y = 2.0
        msg.angular.z = 2.0
        print(msg)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing')
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    turtle_bot_teleop = Turtle_bot_teleop()

    rclpy.spin(turtle_bot_teleop)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    turtle_bot_teleop.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
