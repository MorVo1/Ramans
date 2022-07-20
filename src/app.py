from tkinter import *
import tkinter.colorchooser
from PIL import Image, ImageTk
import tkinter.colorchooser
import customtkinter
import main

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Ramans")
root.geometry('900x900')


# Frame creator
frame_1 = customtkinter.CTkFrame(master=root)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


def show_picture():

    # Opening photo
    main.generate_raman()
    photo = PhotoImage(file='out.png')

    final_img_label = customtkinter.CTkLabel(master=frame_1, image=photo, )
    final_img_label.place(x=600, y=130)


# Buttons
button_generate = customtkinter.CTkButton(master=frame_1, text="GENERATE",
                                          fg_color='#333739', command=show_picture, width=200, height=300, text_font=('Arial', 20))

root.state('zoomed')

button_generate.place(x=200, y=300)

root.mainloop()
