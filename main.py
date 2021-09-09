import tkinter as tk
from tkinter import *
import time
from tanque import TanqueCont
from fogon import caldera

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Hello wold")
    window.configure(bg='grey')
    window.geometry("800x680")

    tanque1=TanqueCont(colorTanque="#19E4A9")
    tanque1.place(x=0, y=0)
    tanque2=TanqueCont(colorTanque="#5D19E4")
    tanque2.place(x=400, y=0)
    cal=caldera(window)
    cal.place(x=200, y=200)
    tanque3=TanqueCont(typeTanque='b', colorTanque="#EDF103")
    tanque3.place(x=200, y=400)
    
    button_inicio = tk.Button(text="Inicio")
    button_inicio.pack()
    button_inicio.place(x=40, y=620)

    button_llT1 = tk.Button(text="LLenar T1", command=tanque1.llenar)
    button_llT1.pack()
    button_llT1.place(x=160, y=620)

    button_llT2 = tk.Button(text="LLenar T2", command=tanque2.llenar)
    button_llT2.pack()
    button_llT2.place(x=280, y=620)

    button_vaciart3 = tk.Button(text="Vaciar T3", command=tanque3.vaciar)
    button_vaciart3.pack()
    button_vaciart3.place(x=420, y=620)

    button_fogon = tk.Button(text="Fogon ⬆")
    button_fogon.pack()
    button_fogon.place(x=560, y=620)

    button_fogon = tk.Button(text="Fogon ⬇")
    button_fogon.pack()
    button_fogon.place(x=695, y=620)







        
    tk.mainloop()

