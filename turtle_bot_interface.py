import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Canvas
from PIL import Image, ImageTk, ImageGrab
import pyautogui
from pynput import keyboard
import os # para acceder a los archivos de la carpeta
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist    #Tipo de mensaje que se publica el topico turtlebot_position
from threading import Thread  #Crear threads para correr dos cosas simultaneamente
from time import sleep

posiciones = [0,0]

def creo_interfaz():
    print("Creo la interfaz")
    root = tk.Tk()
    root.geometry('750x600')
    root.title("turtle_bot_teleop")
    root.configure(bg='#7aebc5')
    name = "gato"
    archivo = os.path.dirname(__file__)
    f = os.path.expanduser(archivo + '/' + name + '.jpeg')
    img = Image.open(f) #modificado para encontrar el path de la foto, si no les sirve descomenten la linea de abajo y comenten esto
    #img = Image.open('gato.jpeg')
    imagen = img.resize((400,400))
    new_image = ImageTk.PhotoImage(imagen)
    etiqueta_imagen = tk.Label(root, image=new_image)
    etiqueta_imagen.place(x=250,y=110)
    ancho = 750
    alto = 600
    pos_x = 400
    pos_y = 300

    ###### draw
        # canvas = Canvas(root)
    canvas = Canvas(root, width = ancho, height = alto)
    canvas.configure(bg='#7aebc5')
    canvas.pack()

        # canvas.create_image(10,10,anchor=tk.NW,image=new_image)

        # img = Image.open("gato.png")
        # imagen = img.resize((400,400))
        # new_image = ImageTk.PhotoImage(imagen)
    canvas.create_image(pos_x,pos_y,image=new_image)

    x1 = pos_x
    y1 = pos_y
    x2 = pos_x + 5
    y2 = pos_y + 5

    text_frame_grafica = tk.Text(root, height=1, width=25,font=("Futura", 20))
    text_frame_grafica.place(x=350,y=30)

    label_grafica = tk.Label(root, text="Introduce el nombre:",bg='#7aebc5',font=("Futura", 20))
    label_grafica.place(x=0,y=32)

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

    open_file_button = tk.Button(root, text="Seleccionar Imagen", command=open_file, height=2, width=20, font=("Futura", 12))
    open_file_button.place(x=30,y=520)

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

    # Crea el botón
    save_screenshot_button = tk.Button(root, text="Tomar pantalla", command=save_screenshot, height=1, width=15, font=("Futura", 12))
    save_screenshot_button.place(x=30,y=450)
    print("AAAAAAAA")
    #canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='blue')
           
    while True:
        print(posiciones[0]) #este dato esta actualizad con el valor que lee el nodo suscriptor
        sleep(0.5) #creo que es mejor quitar esto, solo es para que no muriera mi computador
        canvas.create_rectangle(x1, y1, x2+posiciones[0], y2, fill='blue', outline='blue')
        root.update_idletasks() #estos 2 comandos reemplazan el root.mainloop()
        root.update()
        
            
    



class MinimalSubscriber(Node):
    
    def __init__(self):
        super().__init__('turtle_bot_interface')
        self.subscription = self.create_subscription(Twist, 'turtlebot_position', self.listener_callback, 10) #nodo se suscribe a turtlebot_position
        self.subscription  # prevent unused variable warning
        

    def listener_callback(self, msg):
        #print("listener")
        posiciones[0]  = msg.linear.x #datos requeridos
        posiciones[1] = msg.linear.y
        
    

def main(args=None):
    
    rclpy.init(args=args)
    t = Thread(target=creo_interfaz) #inicia un segundo hilo en el cual va a correr la interfaz
    t.start()
    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)
    #event = Event()
    t.join()
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



