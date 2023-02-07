import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist    #Tipo de mensaje que se publicara al topico turtlebot_cmdVel
from pynput import keyboard   #LIbreria para leer teclado
from pynput.keyboard import Key, Listener



lin = input("Introduzca la velocidad lineal: ")
ang = input("Introduzca la velocidad angular: ")


class Turtle_bot_teleop(Node):

    def __init__(self):

        super().__init__('turtle_bot_teleop')
        self.publisher_ = self.create_publisher(Twist, 'turtlebot_cmdVel', 10)  # no se que poner en tamano de la fila 20
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def on_press(self,key):

        msg = Twist()    

        try:      

            if key.char == "a": #adelante
                msg.linear.x = -float(lin)
                msg.linear.z = 0.0
                msg.angular.z = 0.0
                self.publisher_.publish(msg)
                self.get_logger().info('Izquierda')
                self.i += 1        

            elif key.char == "d": #atras
                
                msg.linear.x = float(lin)
                msg.linear.z = 0.0
                msg.angular.z = 0.0
                self.publisher_.publish(msg)
                self.get_logger().info('Derecha')
                self.i += 1
                
            elif key.char == "l": #giro derecha

                msg.linear.x = 0.0
                msg.linear.z = 0.0
                msg.angular.z = float(ang)
                self.publisher_.publish(msg)
                self.get_logger().info('Giro derecha')
                self.i += 1

            elif key.char == "k": #giro izquierda

                msg.linear.x = 0.0
                msg.linear.z = 0.0
                msg.angular.z = -float(ang)
                self.publisher_.publish(msg)
                self.get_logger().info('Giro izquierda')
                self.i += 1

        except: 

            print("Tecla deshabilitada")


    def on_release(self, key):

        msg = Twist()
        msg.linear.x = 0.0
        msg.linear.z = 0.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.get_logger().info('Stop')
        self.i += 1               

    def timer_callback(self):   #Matar esto y dejar el listener en el init?
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()


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












