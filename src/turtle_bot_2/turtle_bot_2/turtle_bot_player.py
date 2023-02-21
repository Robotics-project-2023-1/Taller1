import rclpy
from rclpy.node import Node
import os
from geometry_msgs.msg import Twist    #Tipo de mensaje que se publicara al topico turtlebot_cmdVel
from turtlebot_interfaces.srv import Reproducir  #Importar el servicio Reproducir


#lin = input("Introduzca la velocidad lineal: ")
#ang = input("Introduzca la velocidad angular: ")

# este nodo levanta el servicio y mueve el robot segun el archivo dado, sin embargo, para llamar el servicio, se debe llamar desde la interfaz o desde 
# la terminal con ros service call

#El servicio recibe un str que es el nombre del archivo y retorna un booleano si se pudo ejecutar

name = None
ejecutar = False

class Turtle_bot_player(Node):

    def __init__(self):

        super().__init__('turtle_bot_player')
        self.publisher_1 = self.create_publisher(Twist, 'turtlebot_cmdVel', 10)  #para publicar a topico al leer el archivo
        self.srv = self.create_service(Reproducir, 'reproducir', self.service_callback) #crear servicio
        self.get_logger().info('Service server ready')

    def service_callback(self, request, response):
        global ejecutar
        global name
        print("recibir nombre")
        self.get_logger().info('Incoming request\na:' + request.nombre)
        name = request.nombre #nombre del archivo a ejecutar
        print(name)
        ejecutar = True
        response.respuesta = True 
        return response

    def mover(self):
        global name
        global ejecutar
        if ejecutar == True: #variable de control para que solo se ejecute una vez el archivo 
            msg_cmdVel = Twist()  
            archivo = os.path.dirname(__file__)
            f = os.path.expanduser(archivo + '/' + name + '.txt')
            with open(f) as text:
                lines = [line.rstrip() for line in text]

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
            ejecutar = False
        else:
            pass

def main(args=None):

    rclpy.init(args=args)
    turtle_bot_player = Turtle_bot_player()
    timer = turtle_bot_player.create_timer(1.0, turtle_bot_player.mover) #timer para el publisher
    rclpy.spin(turtle_bot_player)
    #turtle_bot_player.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
