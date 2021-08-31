import tkinter as tk
from tkinter import *

canvas = Canvas(width=1000, height=600, bg='white')  # Tamaño ventana
canvas.create_oval(100, 10, 180, 80, width=2, fill='blue')
canvas.create_arc(200, 10, 280, 100)
canvas.create_rectangle(10, 100, 200, 200, width=5, fill='red')
canvas.create_text(100, 280, text='tkinter canvas', fill='green')

canvas.pack(expand=YES, fill=BOTH)
canvas.create_line(10, 10, 80, 80)
canvas.create_line(10, 80, 80, 10)

mainloop()


window = tk.Tk()
window.title("Hello wold")
window.geometry("50x50")

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()


tk.mainloop()
