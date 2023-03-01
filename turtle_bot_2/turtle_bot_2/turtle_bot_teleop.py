import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist    #Tipo de mensaje que se publicara al topico turtlebot_cmdVel
from pynput import keyboard   #LIbreria para leer teclado
from pynput.keyboard import Key, Listener
from std_msgs.msg import String #Tipo de mensaje para publicar la tecla presionada al topico turtlebot_teclas

lin = input("Introduzca la velocidad lineal: ")
ang = input("Introduzca la velocidad angular: ")

class Turtle_bot_teleop(Node):

    def __init__(self):

        super().__init__('turtle_bot_teleop')
        self.publisher_1 = self.create_publisher(Twist, 'turtlebot_cmdVel', 10)  # crear publisher
        self.publisher_2 = self.create_publisher(String, 'turtlebot_teclas', 10)  # crear publisher
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def on_press(self,key):

        msg_cmdVel = Twist()  
        msg_tecla = String()  

        try:      

            if key.char == "a": #desplazamiento negativo en el eje x

                msg_tecla.data = "a"
                msg_cmdVel.linear.x = -float(lin)
                msg_cmdVel.angular.z = 0.0
                self.publisher_1.publish(msg_cmdVel) #publicar el mensaje Twist al topico turtlebot_cmdVel
                self.get_logger().info('Izquierda')
                self.publisher_2.publish(msg_tecla) #publicar la tecla al topico turtlebot_teclas
                self.get_logger().info('Izquierda publicada')
                self.i += 1        

            elif key.char == "d": #desplazamiento positivo en el eje x

                msg_tecla.data = "d"
                msg_cmdVel.linear.x = float(lin)
                msg_cmdVel.angular.z = 0.0
                self.publisher_1.publish(msg_cmdVel)
                self.get_logger().info('Derecha')
                self.publisher_2.publish(msg_tecla)
                self.get_logger().info('Derecha publicada')
                self.i += 1
                
            elif key.char == "l": #giro derecha

                msg_tecla.data = "l"
                msg_cmdVel.linear.x = 0.0
                msg_cmdVel.angular.z = float(ang)
                self.publisher_1.publish(msg_cmdVel)
                self.get_logger().info('Giro derecha')
                self.publisher_2.publish(msg_tecla)
                self.get_logger().info('Giro derecha publicada')
                self.i += 1

            elif key.char == "k": #giro izquierda

                msg_tecla.data = "k"
                msg_cmdVel.linear.x = 0.0
                msg_cmdVel.angular.z = -float(ang)
                self.publisher_1.publish(msg_cmdVel)
                self.get_logger().info('Giro izquierda')
                self.publisher_2.publish(msg_tecla)
                self.get_logger().info('Giro izquierda publicada')
                self.i += 1

        except: 

            print("Tecla deshabilitada")


    def on_release(self, key): #si se dejan de presionar teclas, se manda la velocidad del robot a 0

        msg_cmdVel = Twist()
        msg_cmdVel.linear.x = 0.0
        msg_cmdVel.linear.z = 0.0
        msg_cmdVel.angular.z = 0.0
        self.publisher_1.publish(msg_cmdVel)
        self.get_logger().info('Stop')
        self.i += 1               

    def timer_callback(self):   
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()


def main(args=None):

    rclpy.init(args=args)
    turtle_bot_teleop = Turtle_bot_teleop()
    rclpy.spin(turtle_bot_teleop)
    turtle_bot_teleop.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()












