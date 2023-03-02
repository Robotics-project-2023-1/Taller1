import rclpy
from rclpy.node import Node
import os
from geometry_msgs.msg import Twist    #Tipo de mensaje que se publicara al topico turtlebot_cmdVel
from turtlebot_interfaces.srv import Reproducir  #Importar el servicio Reproducir


lin = 10
ang = 10

# este nodo levanta el servicio y mueve el robot segun el archivo dado
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
        self.get_logger().info('Incoming request\na:' + request.nombre) #lee el string con la ubicacion del archivo txt
        name = request.nombre #nombre del archivo a ejecutar
        response.respuesta = True 
        ejecutar = True
        return response

    def mover(self):
        global name
        global ejecutar
        if ejecutar == True: #variable de control para que solo se ejecute una vez el archivo 
            msg_cmdVel = Twist() 
            
            with open(name) as text:
                lines = [line.rstrip() for line in text]

            for i in range(len(lines)):
                
                carac = lines[i]
                print(carac)
                if carac == "a": #eje x negatuvo

                    msg_cmdVel.linear.x = -float(lin)
                    msg_cmdVel.angular.z = 0.0
                    self.publisher_1.publish(msg_cmdVel)
                    self.get_logger().info('Izquierda')   

                elif carac == "d": #eje x positivo

                    msg_cmdVel.linear.x = float(lin)
                    msg_cmdVel.angular.z = 0.0
                    self.publisher_1.publish(msg_cmdVel)
                    self.get_logger().info('Derecha')

                    
                elif carac == "l": #giro derecha

                    msg_cmdVel.linear.x = 0.0
                    msg_cmdVel.angular.z = float(ang)
                    self.publisher_1.publish(msg_cmdVel)
                    self.get_logger().info('Giro derecha')


                elif carac == "k": #giro izquierda

                    msg_cmdVel.linear.x = 0.0
                    msg_cmdVel.angular.z = -float(ang)
                    self.publisher_1.publish(msg_cmdVel)
                    self.get_logger().info('Giro izquierda')

                    
            ejecutar = False
            #dejar de mover una vez se termina de leer el archivo
            msg_cmdVel.linear.x = 0.0
            msg_cmdVel.angular.z = 0.0
            self.publisher_1.publish(msg_cmdVel)
            self.get_logger().info('Parar')
        else:
            pass

def main(args=None):

    rclpy.init(args=args)
    turtle_bot_player = Turtle_bot_player()
    timer = turtle_bot_player.create_timer(1.0, turtle_bot_player.mover) 
    rclpy.spin(turtle_bot_player)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
