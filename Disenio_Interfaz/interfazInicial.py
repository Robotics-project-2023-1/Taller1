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
etiqueta_imagen.place(x=250,y=110)



text_frame_grafica = tk.Text(root, height=1, width=25,font=("Futura", 20))
text_frame_grafica.place(x=350,y=30)

label_grafica = tk.Label(root, text="Introduce el nombre:",bg='#7aebc5',font=("Futura", 20))
label_grafica.place(x=0,y=32)




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

def save_screenshot():
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