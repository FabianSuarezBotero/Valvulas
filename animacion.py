import tkinter as tk
from tkinter import *

canvas = Canvas(width=1000, height=600, bg='white')  # Tamaño ventana

mainloop()

window = tk.Tk()  # Tamaño ventana donde está la foto
window.title("Valvulas")
window.geometry("1000x600")

Tiempo = tk.Label(bg="cyan", text="Tiempo: ")  # Poner la variable de tiempo
# Poner la variable de tiempo
Temp = tk.Label(bg="#DF01D7", text="Temperatura: ")
Tiempo.pack()
Temp.pack()
button = tk.Button(text="INICIO")
button.pack()

canvas = tk.Canvas(window, width=800, height=800)  # Tamaño de la foto
canvas.pack()
img = tk.PhotoImage(file="planta.gif")
canvas.create_image(0, 0, anchor=tk.NW, image=img)

canvas.create_rectangle(68, 85, 180, 150, width=5,
                        fill='pink')  # Nivel tanque 1 lleno
canvas.create_rectangle(290, 85, 400, 152, width=5,
                        fill='cyan')  # Nivel Tanque 2 lleno

# canvas.create_rectangle(68, 85, 180, 150, width=5,fill='white')  # Nivel tanque 1 vacio
# canvas.create_rectangle(290, 85, 400, 152, width=5,fill='white')  # Nivel tanque 2 vacio

canvas.create_line(175, 179, 147, 156, width=5,
                   fill='red')  # Valvula 1 cerrada
canvas.create_line(290, 179, 318, 156, width=5,
                   fill='red')  # Valvula 2 cerrada

canvas.create_line(175, 179, 147, 156, width=5,
                   fill='green')  # Valvula 1 abierta
canvas.create_line(290, 179, 318, 156, width=5,
                   fill='green')  # Valvula 2 abierta

canvas.create_polygon((250, 345, 222, 312, 200, 345),
                      width=4, fill="#DF7401")  # Caldera prendida
# canvas.create_polygon((250, 345, 222, 312, 200, 345),width=4, fill="grey")  # Caldera apagada


tk.mainloop()
