import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageGrab
import pyautogui


# Creación de la ventana principal con la imagen de fondo.

root = tk.Tk()
root.geometry('750x600')
root.title("turtle_bot_teleop")
root.configure(bg='#7aebc5')
img = Image.open("turtlebot3.png")
imagen = img.resize((300,300))
new_image = ImageTk.PhotoImage(imagen)
etiqueta_imagen = tk.Label(root, image=new_image)
etiqueta_imagen.place(x=250,y=110)




# Creación de una etiqueta para mostrar la imagen (cuadro de texto).

#label = tk.Label(root)
#label.pack()

text_frame_grafica = tk.Text(root, height=1, width=25,font=("Futura", 20))
text_frame_grafica.place(x=350,y=30)

label_grafica = tk.Label(root, text="Introduce el nombre:",bg='#7aebc5',font=("Futura", 20))
label_grafica.place(x=0,y=32)



# Creación de un botón para abrir imágenes guardadas.

def open_file():
    file_path = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")))
    try:
        global image
        image = Image.open(file_path)
        render = ImageTk.PhotoImage(image)
        img = tk.Label(root, image=render)
        img.image = render
        img.place(x=100,y=150)
    except:
        messagebox.showerror("Error", "Failed to open the image.")

open_file_button = tk.Button(root, text="Seleccionar Imagen", command=open_file, height=2, width=20, font=("Futura", 12))
open_file_button.place(x=30,y=480)


'''
# Creación de un botón para guardar la imagen.

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")))
    try:
        image.save(file_path)
        messagebox.showinfo("Success", "Image saved successfully.")
    except:
        messagebox.showerror("Error", "Failed to save the image.")

save_file_button = tk.Button(root, text="Guardar imagen", height=3, width=30, command=save_file, font=("Futura", 16))
save_file_button.place(x=30,y=480)
'''

# Creación de un botón para tomar un pantallazo de la interfaz.

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
save_screenshot_button = tk.Button(root, text="Tomar pantalla", command=save_screenshot, height=1, width=15, font=("Futura", 12))
save_screenshot_button.place(x=30,y=430)

# Run the main loop
root.mainloop()


'''
# Creación de un botón para tomar un pantallazo de la interfaz.

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

    #image.save("screenshot.png")

# Crea el botón
save_file_button = tk.Button(root, text="Tomar pantalla", command=take_screenshot, height=1, width=15, font=("Futura", 16))
save_file_button.place(x=30,y=350)
'''


'''
#Creación del botón de guardar imagen. Se abre una imagen y se guarda al cambiarle el nombre.

def save_image():
    # You need to replace 'image.jpg' with the path to the image you want to save
    texto = str(text_frame_grafica)
    image = Image.open("johann_osma.jpg")
    image.save(texto + ".jpg")

save_file_button = tk.Button(root, text="Guardar imagen", height=3, width=30, command=save_image, font=("Futura", 16))
save_file_button.place(x=30,y=480)
'''





'''
# Creación de un botón para tomar un pantallazo de toda la pantalla.

def take_screenshot():

    # Obtiene una copia de la ventana actual
    image = ImageGrab.grab()

    # Guarda la imagen en un archivo
    image.save("screenshot.png")


# Crea el botón
save_file_button = tk.Button(root, text="Tomar pantalla", command=take_screenshot, height=1, width=15, font=("Futura", 16))
save_file_button.place(x=30,y=350)

# Run the main loop
root.mainloop()
'''