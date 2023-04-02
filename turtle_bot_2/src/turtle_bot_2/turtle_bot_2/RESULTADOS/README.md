Taller 1: Turtlebot_2

Para abrir el entorno de la simulación se ejecuta:
>>>>>>>>> nueva terminal: 
$ cd Downloads/Coppelia
$ ./coppeliaSim.sh 

Dentro de este entorno se debe cargar el archivo .ttt correspondiente a la escena. 

*Nota: Para la ejecución de este taller se utlizan las librerías de python: pynput, pyautogui, PIL, tkinter

El primer paso es realizar los comandos:
$ cd turtle_bot_2
$ colcon build

Para realizar el control del robot (punto 1) se usan las teclas a,d,k,l. Para velocidad lineal y angular.
Esto se hace con los siguientes comandos:
>>>>>>>>> nueva terminal:
$ source /opt/ros/humble/setup.bash
$ cd turtle_bot_2
$ . install/local_setup.bash
$ ros2 run turtle_bot_2 turtle_bot_teleop


Para correr únicamente la interfaz se utilizan los comandos:
>>>>>>>>> nueva terminal:
$ source /opt/ros/humble/setup.bash
$ cd turtle_bot_2
$ . install/local_setup.bash
$ ros2 run turtle_bot_2 turtle_bot_interface

En esta interfaz se pueden seleccionar imagenes y estas se muestran escaladas a 400x400. 
También se pueden guardar con el nombre ingresado en la barra superior. (punto 2 ) 
Para ver el recorrido del robot al moverse se debe ejecutar en otra terminal:
>>>>>>>>> nueva terminal:
$ source /opt/ros/humble/setup.bash
$ cd turtle_bot_2
$ . install/local_setup.bash
$ ros2 run turtle_bot_2 turtle_bot_teleop

>>>>>>>>> nueva terminal:
$ source /opt/ros/humble/setup.bash
$ cd turtle_bot_2
$ . install/local_setup.bash
$ ros2 run turtle_bot_2 turtle_bot_player

Se puede guardar un archivo .txt con las teclas presionadas (punto 3)


Finalmente para realizar un recorrido guardado en un archivo .txt (punto 4) en caso de que no se estén corriendo ya, se deben correr
los nodos turtle_bot_player y turtle_bot_interface.
>>>>>>>>> nueva terminal:
$ source /opt/ros/humble/setup.bash
$ cd turtle_bot_2
$ . install/local_setup.bash
$ ros2 run turtle_bot_2 turtle_bot_player
>>>>>>>>> nueva terminal:
$ source /opt/ros/humble/setup.bash
$ cd turtle_bot_2
$ . install/local_setup.bash
$ ros2 run turtle_bot_2 turtle_bot_interface

Al presionar el botón de cargar recorrido se debe ejecutar el servicio y el robot se moverá según las teclas. 




