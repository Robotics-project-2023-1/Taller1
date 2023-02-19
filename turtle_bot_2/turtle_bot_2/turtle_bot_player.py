''''
import rclpy
from rclpy.node import Node

class MinimalService(Node):
    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))
        return response

    def main(args=None):
        rclpy.init(args=args)
        minimal_service = MinimalService()
        rclpy.spin(minimal_service)
        rclpy.shutdown()
    
if __name__ == '__main__':
    main()
'''
import os
name = "Tecla"
archivo = os.path.dirname(__file__)
f = os.path.expanduser(archivo + '/' + name + '.txt')
#nom = open(f,"a")
#nom.write("a \n")
#nom.write("b \n")
#nom.write("c \n")

with open(f) as text:
    lines = [line.rstrip() for line in text]


# este nodo levanta el servicio y mueve el robot segun el archivo dado, sin embargo, para llamar el servicio, se debe llamar desde la interfaz o desde 
# la terminal con ros service call

'''
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist    #Tipo de mensaje que se publica el topico turtlebot_position
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Canvas
from PIL import Image, ImageTk, ImageGrab
import pyautogui
from pynput import keyboard
import os # para acceder a los archivos de la carpeta
def open_file():
    file_path = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")))
    try:
        global image
        image = Image.open(file_path)
        image = image.resize((400,400))
        render = ImageTk.PhotoImage(image)
        img = tk.Label(root, image=render)
        img.image = render
        # img.place(x=100,y=150)
        canvas.create_image(pos_x,pos_y,image=render)
    except:
        messagebox.showerror("Error", "Failed to open the image.")

def save_screenshot():
        x = root.winfo_rootx()
        y = root.winfo_rooty()
        width = root.winfo_width()
        height = root.winfo_height()
        
        # # para ubuntu:
        # # Crea una imagen a partir de la ventana actual
        ####### hacer estos pasos en consola para que funcione:
        # # 1. $ sudo nano /etc/gdm3/custom.conf
        # # 2. $ WaylandEnable=false
        # # 3. guardar los cambios
        # # 4. $ sudo systemctl restart gdm3
        image = pyautogui.screenshot(region=(x+200, y+100, width-350, height-200))
        
        # # para Windows:
        # Crea una imagen a partir de la ventana actual
        # dx = (width-750)/2
        # image = ImageGrab.grab((x+dx+200, y+100, x+dx+600, y + 500))

        # Guarda la imagen en un archivo
        texto = str(text_frame_grafica.get("1.0",'end-1c'))
        file_path = filedialog.asksaveasfilename(defaultextension=".png", initialfile= texto + ".png", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")))
        image.save(file_path)

def abrir_interfaz():
    root = tk.Toplevel()
    root.geometry('750x600')
    root.title("turtle_bot_teleop")
    root.configure(bg='#7aebc5')
    name = "gato"
    archivo = os.path.dirname(__file__)
    f = os.path.expanduser(archivo + '/' + name + '.jpeg')
    img = Image.open(f)
    imagen = img.resize((400,400))
    new_image = ImageTk.PhotoImage(imagen, master = root)
    etiqueta_imagen = tk.Label(root, image=new_image)
    etiqueta_imagen.place(x=250,y=110)

    ancho = 750
    alto = 600
    pos_x = 400
    pos_y = 300

    ###### draw
    canvas = Canvas(root, width = ancho, height = alto)
    canvas.configure(bg='#7aebc5')
    canvas.pack()

    canvas.create_image(pos_x,pos_y,image=new_image)

    x1 = pos_x
    y1 = pos_y
    x2 = pos_x + 5
    y2 = pos_y + 5

    text_frame_grafica = tk.Text(root, height=1, width=25,font=("Futura", 20))
    text_frame_grafica.place(x=350,y=30)

    label_grafica = tk.Label(root, text="Introduce el nombre:",bg='#7aebc5',font=("Futura", 20))
    label_grafica.place(x=0,y=32)

    open_file_button = tk.Button(root, text="Seleccionar Imagen", command=open_file, height=2, width=20, font=("Futura", 12))
    open_file_button.place(x=30,y=520)


    # Crea el botón
    save_screenshot_button = tk.Button(root, text="Tomar pantalla", command=save_screenshot, height=1, width=15, font=("Futura", 12))
    save_screenshot_button.place(x=30,y=450)

    # incluir el boton del archivo
    # if quiero guardar el archivo: nombre = algo
    nombre = "a"
    av_x = 0
    av_y = 0
    canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='blue')


    return nombre



class MinimalSubscriber(Node):

    

    def __init__(self):
        super().__init__('turtle_bot_interface')
        self.subscription = self.create_subscription(Twist, 'turtlebot_position', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning
        nombre_txt = abrir_interfaz()

        if nombre_txt is not None:
            pass
           # almacenar_teclas(self)
    

    def listener_callback(self, msg):
        self.get_logger().info('I heard x: "%s"' % msg.linear.x)
        self.get_logger().info('I heard y: "%s"' % msg.linear.y)
        self.get_logger().info('I heard z: "%s"' % msg.linear.z)
        canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='blue')

    

def main(args=None):
    abrir_interfaz()
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()



'''