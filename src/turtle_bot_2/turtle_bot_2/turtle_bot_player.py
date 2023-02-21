import rclpy
from rclpy.node import Node
import os
from geometry_msgs.msg import Twist    #Tipo de mensaje que se publicara al topico turtlebot_cmdVel
from turtlebot_interfaces.srv import Reproducir


lin = input("Introduzca la velocidad lineal: ")
ang = input("Introduzca la velocidad angular: ")

#nom = open(f,"a")
#nom.write("a \n")
#nom.write("b \n")
#nom.write("c \n")

#name = "Tecla"
#archivo = os.path.dirname(__file__)
#f = os.path.expanduser(archivo + '/' + name + '.txt')

#with open(f) as text:
#    lines = [line.rstrip() for line in text]


# este nodo levanta el servicio y mueve el robot segun el archivo dado, sin embargo, para llamar el servicio, se debe llamar desde la interfaz o desde 
# la terminal con ros service call

name = None
class Turtle_bot_player(Node):

    def __init__(self):

        super().__init__('turtle_bot_player')
        #self.publisher_1 = self.create_publisher(Twist, 'turtlebot_cmdVel', 10)  # 
        print("init")
        self.srv = self.create_service(Reproducir, 'reproducir', self.recibir_nombre_callback)
        #timer_period = 0.5  # seconds
        #self.timer = self.create_timer(timer_period, self.recibir_nombre_callback)
        #self.i = 0

    def recibir_nombre_callback(self, request, response):
        print("recibir nombre")
        response.respuesta = True 
        self.get_logger().info('Incoming request\na: %d' % (request.nombre))
        name = request.nombre
        print(name)
        return response
    '''
    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1
    
    def mover(self):

        msg_cmdVel = Twist()  
        for i in range(len(lines)):
            carac = lines[i]

            if carac == "a": #izquierda

                msg_cmdVel.linear.x = -float(lin)
                msg_cmdVel.linear.z = 0.0
                msg_cmdVel.angular.z = 0.0
                self.publisher_1.publish(msg_cmdVel)
                self.get_logger().info('Izquierda')
                self.i += 1        

            elif carac == "d": #derecha

                msg_cmdVel.linear.x = float(lin)
                msg_cmdVel.linear.z = 0.0
                msg_cmdVel.angular.z = 0.0
                self.publisher_1.publish(msg_cmdVel)
                self.get_logger().info('Derecha')
                self.i += 1
                
            elif carac == "l": #giro derecha

                msg_cmdVel.linear.x = 0.0
                msg_cmdVel.linear.z = 0.0
                msg_cmdVel.angular.z = float(ang)
                self.publisher_1.publish(msg_cmdVel)
                self.get_logger().info('Giro derecha')
                self.i += 1

            elif carac == "k": #giro izquierda

                msg_cmdVel.linear.x = 0.0
                msg_cmdVel.linear.z = 0.0
                msg_cmdVel.angular.z = -float(ang)
                self.publisher_1.publish(msg_cmdVel)
                self.get_logger().info('Giro izquierda')
                self.i += 1
    '''

def main(args=None):

    rclpy.init(args=args)
    turtle_bot_player = Turtle_bot_player()
    rclpy.spin(turtle_bot_player)
    #turtle_bot_player.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
