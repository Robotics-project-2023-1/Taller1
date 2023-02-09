import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

# Create the window
root = tk.Tk()
root.geometry('700x700')
root.title("turtle_bot_teleop")
root.configure(bg='#7aebc5')


text_frame_grafica = tk.Text(root, height=1, width=25,font=("Futura", 20))
text_frame_grafica.place(x=350,y=30)

label_grafica = tk.Label(root, text="Introduce el nombre de la gráfica:",bg='#7aebc5',font=("Futura", 20))
label_grafica.place(x=20,y=32)


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

