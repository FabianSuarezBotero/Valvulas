import tkinter as tk
from tkinter import *
import time

canvas = Canvas(width=1000, height=600, bg='white')  # Tamaño ventana

mainloop()

window = tk.Tk()  # Tamaño ventana donde está la foto
window.title("Valvulas")
window.geometry("1000x600")

Tiempo = tk.Label(bg="cyan", text="Tiempo: ")  # Poner la variable de tiempo

# Poner la variable de temperatura
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
canvas.create_rectangle(300, 398, 486, 463, width=5,
                        fill='white')  # Tanque 3 vacio
canvas.create_line(160, 179, 160, 156, width=5,
                   fill='red')  # Valvula 1 cerrada
canvas.create_line(306, 179, 306, 156, width=5,
                   fill='red')  # Valvula 2 cerrada
canvas.create_line(309, 312, 309, 334, width=5,
                   fill='red')  # Valvula 3 cerrada
canvas.create_polygon((250, 345, 222, 312, 200, 345),
                      width=4, fill="grey")  # Caldera apagada

# Inicio del proceso

if inicio == true:
    # Valvula 1 cerrada borrada
    canvas.create_line(160, 179, 160, 156, width=5, fill='white')
    canvas.create_line(175, 179, 147, 156, width=5,
                       fill='green')  # Valvula 1 abierta
    canvas.create_rectangle(157, 305, 320, 260, width=5,
                            fill='pink')  # Caldera nivel 1
    canvas.create_rectangle(68, 85, 180, 150, width=5,
                            fill='white')  # Nivel tanque 1 vacio
    canvas.create_polygon((250, 345, 222, 312, 200, 345),
                          width=4, fill="#DF7401")  # Caldera prendida
    time.sleep(5)

    if temp >= 80:
        # Valvula 3 cerrada borrada
        canvas.create_line(309, 312, 309, 334, width=5, fill='white')
        canvas.create_line(294, 312, 322, 334, width=5,
                           fill='green')  # Valvula 3 abierta
        # Tanque 3 con nivel 1
        canvas.create_rectangle(300, 423, 486, 463, width=5, fill='pink')
        # Caldera nivel 1 vacia
        canvas.create_rectangle(157, 305, 320, 260, width=5, fill='white')

    elif temp < 80:
        # Valvula 2 cerrada borrada
        canvas.create_line(306, 179, 306, 156, width=5, fill='white')
        canvas.create_line(290, 179, 318, 156, width=5,
                           fill='green')  # Valvula 2 abierta
        # Nivel tanque 2 vacio
        canvas.create_rectangle(290, 85, 400, 152, width=5, fill='white')
        canvas.create_rectangle(
            157, 220, 320, 255, width=5, fill='cyan')  # Caldera nivel 2
        # NO SE COMO PONER QUE LLEGUE A LOS 80 GRADOS
        # Valvula 3 cerrada borrada
        canvas.create_line(309, 312, 309, 334, width=5, fill='white')
        canvas.create_line(294, 312, 322, 334, width=5,
                           fill='green')  # Valvula 3 abierta
        # Caldera nivel 1 vacia
        canvas.create_rectangle(157, 305, 320, 260, width=5, fill='white')
        # Caldera nivel 2 vacia
        canvas.create_rectangle(157, 220, 320, 255, width=5, fill='white')
        # Tanque 3 con nivel 1
        canvas.create_rectangle(300, 423, 486, 463, width=5, fill='pink')
        # Tanque 3 con nivel 2
        canvas.create_rectangle(300, 383, 486, 420, width=5, fill='cyan')

tk.mainloop()
