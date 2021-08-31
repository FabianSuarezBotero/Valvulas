import tkinter as tk
from tkinter import *

canvas = Canvas(width=1000, height=600, bg='white')  # Tamaño ventana

mainloop()

window = tk.Tk()  # Tamaño ventana donde está la foto
window.title("Valvulas")
window.geometry("1000x600")

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()

canvas = tk.Canvas(window, width=800, height=800)  # Tamaño de la foto
canvas.pack()
img = tk.PhotoImage(file="planta.gif")
canvas.create_image(0, 0, anchor=tk.NW, image=img)

tk.mainloop()
