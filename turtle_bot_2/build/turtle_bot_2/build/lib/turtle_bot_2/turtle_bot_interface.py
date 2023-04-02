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
from std_msgs.msg import String
from threading import Thread  #Crear threads para correr dos cosas simultaneamente
from time import sleep
from turtlebot_interfaces.srv import Reproducir #servicio


global quiero_txt
quiero_txt = False
nombre_txt = None 
guardar_movimientos = False
filename = None
folder_path = None

posiciones = [0,0]
tecla_presionada = '.'
keys_pressed = []


def creo_interfaz():
    print("Creo la interfaz")
    root = tk.Tk()
    root.geometry('850x600')
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
    ancho = 800
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

    text_frame_grafica = tk.Text(root, height=1, width=25,font=("Futura", 15))
    text_frame_grafica.place(x=350,y=26)

    label_grafica = tk.Label(root, text="Introduce el nombre de la imagen:",bg='#7aebc5',font=("Futura", 15))
    label_grafica.place(x=0,y=26)

    text_frame_archivo = tk.Text(root, height=1, width=25,font=("Futura", 15))
    text_frame_archivo.place(x=350,y=65)

    label_grafica = tk.Label(root, text="Introduce el nombre del archivo:",bg='#7aebc5',font=("Futura", 15))
    label_grafica.place(x=0,y=65)

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

    open_file_button = tk.Button(root, text="Seleccionar Imagen", command=open_file, height=2, width=17, font=("Futura", 11))
    open_file_button.place(x=10,y=520)

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
        image = pyautogui.screenshot(region=(x+224, y+100, width-450, height-200))
        
        
        # # para Windows:
        # Crea una imagen a partir de la ventana actual
        # dx = (width-750)/2
        # image = ImageGrab.grab((x+dx+200, y+100, x+dx+600, y + 500))

        # Guarda la imagen en un archivo
        texto = str(text_frame_grafica.get("1.0",'end-1c'))
        file_path = filedialog.asksaveasfilename(defaultextension=".png", initialfile= texto + ".png", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")))
        image.save(file_path)
    
    def read_txt():
        # solicitar servicio con el nombre del archivo
        global quiero_txt
        global nombre_txt
        try:
            file_path = filedialog.askopenfilename()
            nombre = os.path.basename(file_path)
            nombre_txt = file_path 
            print(nombre_txt)
            quiero_txt = True 
            print("en funcion read_txt pasa a ser True")     
        except:
            quiero_txt = False
    
    def save_to_txt(): #PONER LO DE LEER TECLAS
        global guardar_movimientos
        global filename
        global folder_path
        print("nombre archivo")
        filename = text_frame_archivo.get('1.0',tk.END).strip()
        folder_path = filedialog.askdirectory()
        guardar_movimientos = True
        with open(folder_path + '/' + filename + ".txt", "w") as file:
            for key in keys_pressed:
                file.write(key + '\n')
        pass

        # Crear botones
    save_screenshot_button = tk.Button(root, text="Tomar pantalla", command=save_screenshot, height=2, width=17, font=("Futura", 11))
    save_screenshot_button.place(x=10,y=450)

    save_text_button = tk.Button(root, text="Guardar movimientos", command = save_to_txt, height=2, width=19, font=("Futura", 11))
    save_text_button.place(x=630, y=520)

    read_movements_button = tk.Button(root, text="Reproducir movimientos", command = read_txt, height=2, width=19, font=("Futura", 11))
    read_movements_button.place(x= 630, y = 450)

    #QUE ESTA VAINA DEVUELVA EL NOMBRE DEL ARCHIVO Y ACTIVE UN BOOLEANO PARA LLAMAR AL SERVICIO

    #print("AAAAAAAA")
    #canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='blue')
           
    while True:
        print("dibujando")
        print(posiciones)
        xd = (posiciones[0]+2.27)*88.3+200
        yd = ((posiciones[1]+2.27)*88.3-402.5)*(-1)+95
        # print('x: '+str(xd)+', y: '+str(yd)) 
        sleep(0.2) #creo que es mejor quitar esto, solo es para que no muriera mi computador
        canvas.create_rectangle(xd, yd, xd+2, yd+2, fill='blue', outline='blue')
        root.update_idletasks() #estos 2 comandos reemplazan el root.mainloop()
        root.update()
        
'''
def leo_teclas():
    global guardar_movimientos 
    global filename
    def on_press(key):       
        if guardar_movimientos == True:
            with open(folder_path + '/' + filename + ".txt", "w") as file:
                print("archivo abierto y guardando")
                file.write(key + '\n')


    def on_release(key):
        pass

    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
        
'''

class Turtle_bot_interface(Node):
    
    def __init__(self):
        global quiero_txt
        super().__init__('turtle_bot_interface')
        self.subscription = self.create_subscription(Twist, 'turtlebot_position', self.listener_callback_posicion, 10) #nodo se suscribe a turtlebot_position
        self.subscription  # prevent unused variable warning
        self.subscription = self.create_subscription(String, 'turtlebot_teclas', self.listener_callback_teclas, 10) #nodo se suscribe a turtlebot_teclas
        self.subscription  # prevent unused variable warning
        # quiero_txt = True #ESTO SE DEBE DEFINIR EN EL BOTON DEL TXT Y TAMBIEN SE DEBE ALMACENAR EL NOMBRE DEL TXT COMO nombre_txt
        
        self.cli = self.create_client(Reproducir, 'reproducir')
        print("cliente creado")
        while not self.cli.wait_for_service(timeout_sec=2.0):
                self.get_logger().info('service not available, waiting again...')
        
        
    def send_request(self, nombre_txt):
        global quiero_txt
        if quiero_txt == True:  #ESTE ES EL BOOLEANO QUE ACTIVA EL SERVICIO
            self.request = Reproducir.Request()
            self.request.nombre = nombre_txt
            self.future = self.cli.call_async(self.request)
            rclpy.spin_until_future_complete(self, self.future)
            if self.future.result() is not None:
                response = self.future.result()
                if response.respuesta:
                    print("SIUUUU, PONER ALGO EN LA INTERFAZ QUE DIGA COMO 'EJECUTANDO' O ALGO ASI")
                else:
                    print("NOUUU")
            else:
                self.get_logger().error('Service call failed')
            quiero_txt = False

    def listener_callback_posicion(self, msg):
        #print("escuchando")
        global quiero_txt
        global nombre_txt
        #print("listener")
        posiciones[0]  = msg.linear.x #datos requeridos
        posiciones[1] = msg.linear.y
        if quiero_txt == True:
            print("voy a mandar request")
            self.send_request(nombre_txt)
            quiero_txt = False
            
    def listener_callback_teclas(self, msg):
        # print(msg.data)
        tecla_presionada = msg.data
        keys_pressed.append(tecla_presionada)
        
        

def main(args=None):
    
    rclpy.init(args=args)
    t = Thread(target=creo_interfaz) #inicia un segundo hilo en el cual va a correr la interfaz
    t.start()
    #t2 = Thread(target=leo_taclas) #inicia un tercer hilo para leer las teclas
    turtle_bot_interface = Turtle_bot_interface() 
    #turtle_bot_interface.send_request(nombre_txt)
    #turtle_bot_interface.get_logger().info('Resultado: %d' % (response.respuesta))
    rclpy.spin(turtle_bot_interface)
    t.join()
    turtle_bot_interface.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
