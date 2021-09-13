import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
from Tanque import TanqueCont
from caldera import Fogon


def aviso():
    messagebox.showinfo(message="No", title="Título")


def main():
    window = tk.Tk()
    window.title("Proceso")
    window.configure(bg='grey')
    window.geometry("800x680")

    tanque1 = TanqueCont(window, colorTanque="#19E4A9")
    tanque1.place(x=0, y=0)
    tanque2 = TanqueCont(window, colorTanque="#5D19E4")
    tanque2.place(x=400, y=0)
    cal = Fogon(window)
    cal.place(x=200, y=200)
    tanque3 = TanqueCont(window, typeTanque='b', colorTanque="#EDF103")
    tanque3.place(x=196, y=400)

    def iniciar():
        print(tanque2.estado(), tanque1.estado())
        if tanque1.estado() == True and tanque2.estado() == True:
            tanque1.vaciar()
            cal.llenado1()
            cal.mostrar_temp()
        else:
            aviso()

    button_inicio = tk.Button(window, text="Inicio", command=iniciar)
    button_inicio.pack()
    button_inicio.place(x=40, y=620)

    button_llT1 = tk.Button(window, text="LLenar T1", command=tanque1.llenar)
    button_llT1.pack()
    button_llT1.place(x=160, y=620)

    button_llT2 = tk.Button(window, text="LLenar T2", command=tanque2.llenar)
    button_llT2.pack()
    button_llT2.place(x=280, y=620)

    button_vaciart3 = tk.Button(
        window, text="Vaciar T3", command=tanque3.vaciar)
    button_vaciart3.pack()
    button_vaciart3.place(x=420, y=620)

    button_fogon = tk.Button(window, text="Fogon ⬆",
                             command=cal.subir_temperatura)
    button_fogon.pack()
    button_fogon.place(x=560, y=620)

    button_fogon = tk.Button(window, text="Fogon ⬇",
                             command=cal.bajar_temperatura)
    button_fogon.pack()
    button_fogon.place(x=695, y=620)

    tk.mainloop()


main()
