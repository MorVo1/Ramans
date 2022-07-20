from tkinter import *
import tkinter.colorchooser
from PIL import Image, ImageTk
import tkinter.colorchooser
import main

root = Tk()
root.geometry("1000x754")
root.title('Ramans')
root.state('zoomed')
root.resizable(0, 0)

# resizing background
img = Image.open("background.png")
resized = img.resize((2000, 1200), Image.Resampling.LANCZOS)
resized.save("background.png")

# Define the PhotoImage Constructor by passing the image file
img = PhotoImage(file='background.png', master=root)
img_label = Label(root, image=img, bg='grey')


#  define the position of the image
img_label.place(x=0, y=0)

final_img_label = Label(root)
final_img_label.place(x=600, y=150, width=640,  height=640)


def show_picture():

    # Opening photo
    main.generate_raman()
    photo = PhotoImage(file='out.png')

    final_img_label = Label(root, image=photo)
    final_img_label.place(x=600, y=150)


# Buttons
button_generate = Button(root, text="GENERATE", pady=50, padx=80,
                         fg='white', bg='black', command=show_picture)
# Window maximized
root.state('zoomed')

button_generate.place(x=200, y=300)

root.mainloop()
