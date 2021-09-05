import tkinter as tk
from tkinter import *
import time

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Hello wold")
    window.geometry("800x680")
    
    button_inicio = tk.Button(text="Inicio")
    button_inicio.pack()
    button_inicio.place(x=80, y=620)

    button_llCalT1 = tk.Button(text="LLenar Caldera con T1")
    button_llCalT1.pack()
    button_llCalT1.place(x=170, y=620)

    button_fogon = tk.Button(text="Fogon")
    button_fogon.pack()
    button_fogon.place(x=350, y=620)

    button_vaciar = tk.Button(text="Vaciar Caldera")
    button_vaciar.pack()
    button_vaciar.place(x=450, y=620)

    button_llCalT2 = tk.Button(text="LLenar Caldera con T2")
    button_llCalT2.pack()
    button_llCalT2.place(x=600, y=620)

    tanque = Canvas( width = 200, height = 200, bg = 'black', highlightthickness=0) 
    tanque.place(x=50,y=50)
    tanque.create_rectangle(140,20,10,180, fill= "#000fff000")
    tanque.pack()
        
    tk.mainloop()

