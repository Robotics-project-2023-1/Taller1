import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageGrab
import pyautogui

root = tk.Tk()
root.geometry('750x600')
root.title("turtle_bot_teleop")
root.configure(bg='#7aebc5')
img = Image.open("turtlebot3.png")
imagen = img.resize((300,300))
new_image = ImageTk.PhotoImage(imagen)
etiqueta_imagen = tk.Label(root, image=new_image)
etiqueta_imagen.place(x=250,y=90)



text_frame_grafica = tk.Text(root, height=1, width=25,font=("Futura", 20))
text_frame_grafica.place(x=350,y=30)

label_grafica = tk.Label(root, text="Introduce el nombre de la gráfica:",bg='#7aebc5',font=("Futura", 20))
label_grafica.place(x=20,y=32)


def save_screenshot():
    # Obtiene una copia de la ventana actual
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    width = root.winfo_width()
    height = root.winfo_height()

    # Crea una imagen a partir de la ventana actual
    image = ImageGrab.grab((x, y, x + width, y + height))

    # Guarda la imagen en un archivo
    texto = str(text_frame_grafica.get("1.0",'end-1c'))
    image.save(texto + ".png")

# Crea el botón
save_screenshot_button = tk.Button(root, text="Tomar pantalla", command=save_screenshot, height=1, width=15, font=("Futura", 16))
save_screenshot_button.place(x=30,y=350)


root.mainloop()

'''
import tkinter as tk
import pyautogui
from PIL import Image, ImageTk


root = tk.Tk()
root.geometry('750x750')
root.title("turtle_bot_teleop")
root.configure(bg='#7aebc5')

text_frame_grafica = tk.Text(root, height=1, width=25, font=("Futura", 20))
text_frame_grafica.place(x=350, y=30)

label_grafica = tk.Label(root, text="Introduce el nombre de la gráfica:", bg='#7aebc5', font=("Futura", 20))
label_grafica.place(x=20, y=32)

def take_screenshot():
    x = root.winfo_x()
    y = root.winfo_y()
    width = root.winfo_width()
    height = root.winfo_height()

    # Obtiene una copia de la ventana actual
    image = pyautogui.screenshot(region=(x, y, width, height))

    # Guarda la imagen en un archivo
    texto = str(text_frame_grafica.get("1.0",'end-1c'))
    image.save(texto + ".png")


save_file_button = tk.Button(root, text="Tomar pantalla", command=take_screenshot, height=1, width=15, font=("Futura", 16))
save_file_button.place(x=30, y=350)

root.mainloop()
'''


'''
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Create a text entry widget
entry = Entry(root)
entry.pack()

# Create a button that saves the image
def save_image():
    name = entry.get()
    # You need to replace 'image.jpg' with the path to the image you want to save
    image = Image.open("johann_osma.jpg")
    image.save(name + ".jpg")

button = Button(root, text="Save Image", command=save_image)
button.pack()

root.mainloop()
'''


##################

'''
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

# Create the window
root = tk.Tk()
root.geometry('750x750')
root.title("turtle_bot_teleop")
root.configure(bg='#7aebc5')


text_frame_grafica = tk.Text(root, height=1, width=25,font=("Futura", 20))
text_frame_grafica.place(x=350,y=30)

label_grafica = tk.Label(root, text="Introduce el nombre de la gráfica:",bg='#7aebc5',font=("Futura", 20))
label_grafica.place(x=20,y=32)



# Create an Open File button
def open_file():
    file_path = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")))
    try:
        global image
        image = Image.open(file_path)
        render = ImageTk.PhotoImage(image)
        img = tk.Label(root, image=render)
        img.image = render
        img.pack()
    except:
        messagebox.showerror("Error", "Failed to open the image.")

open_file_button = tk.Button(root, text="Open File", command=open_file)
open_file_button.pack()


# Create a Save button
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")))
    try:
        image.save(file_path)
        messagebox.showinfo("Success", "Image saved successfully.")
    except:
        messagebox.showerror("Error", "Failed to save the image.")

save_file_button = tk.Button(root, text="Guardar imagen",height=3,width=30, command=save_file,font=("Futura", 16))
save_file_button.place(x=50,y=600)



# Run the main loop
root.mainloop()
'''


##################################


'''
import tkinter as tk

root = tk.Tk()
imagen = tk.PhotoImage(file="turtlebot3.png")
etiqueta_imagen = tk.Label(root, image=imagen)
etiqueta_imagen.pack()
root.mainloop()
'''


#################################

'''
import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab

def take_screenshot():
    # Obtiene una copia de la ventana actual
    image = ImageGrab.grab()

    # Guarda la imagen en un archivo
    image.save("screenshot.png")

# Crea la ventana principal
root = tk.Tk()
root.title("Capturador de pantalla")

# Crea el botón
button = tk.Button(root, text="Tomar pantalla", command=take_screenshot)
button.pack()

# Ejecuta el bucle de eventos
root.mainloop()
'''