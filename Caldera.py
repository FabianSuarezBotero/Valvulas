from tkinter import *
import time
from random import *


class Caldera:
    def __init__(self, pantalla):
        frame = Frame(pantalla)
        frame.config(width=800, height=200, bg="blue", highlightthickness=0)
        frame.pack(padx=10, pady=10)

        caldera = Canvas(frame, width=800, height=200, bg='white')
        caldera.place(x=100, y=100)
        caldera.create_rectangle(140, 20, 320, 180, fill="pink")
        caldera.create_oval(140, 175, 320, 190, fill="green")
        caldera.create_oval(140, 0, 320, 35, fill="green")

        caldera.create_rectangle(160, 55, 300, 165, fill="white")
        caldera.create_rectangle(160, 165, 300, 165, fill="blue")
        caldera.create_oval(160, 160, 300, 170, fill="red")
        caldera.create_oval(160, 50, 300, 60, fill="red")

        caldera.create_polygon(100, 140, 70, 185, 130, 185, fill='grey')
        caldera.create_polygon(100, 85, 70, 130, 130, 130, fill='orange')
        caldera.create_polygon(100, 30, 70, 75, 130, 75, fill='red')

        nombre1 = Label(raiz, text="Nivel 2", bg="black",
                        fg="white", font="Helvetica 12 bold")
        nombre1.pack()
        nombre1.place(x=335, y=50)

        nombre2 = Label(raiz, text="Nivel 1", bg="black",
                        fg="white", font="Helvetica 12 bold")
        nombre2.pack()
        nombre2.place(x=335, y=110)

        def llenado1():
            num = 165
            for i in range(110, num):
                caldera.create_rectangle(160, 55, 300, 165, fill="white")
                caldera.create_rectangle(160, num, 300, 165, fill="blue")
                caldera.update()

                time. sleep(0.015)
                num = num - 1
                N = int((i-64)*250)

        def llenado2():
            num = 110
            for i in range(55, num):
                caldera.create_rectangle(160, 55, 300, 165, fill="white")
                caldera.create_rectangle(160, num, 300, 165, fill="blue")
                caldera.update()

                time. sleep(0.015)
                num = num - 1
                N = int((i-64)*250)

        def vaciado():
            for a in range(55, 165):
                caldera.create_rectangle(160, 55, 300, 165, fill="white")
                caldera.create_rectangle(160, a, 300, 165, fill="blue")
                caldera.update()

                time.sleep(0.015)
                l = int(25000 - (a-64)*250)

        caldera.pack()

        boton = Button(raiz, bg="magenta", text="LLENAR1",
                       command=llenado1, width=15)
        boton.pack()
        boton. place(x=380, y=120)

        boton3 = Button(raiz, bg="magenta", text="LLENAR2",
                        command=llenado2, width=15)
        boton3.pack()
        boton3. place(x=380, y=80)

        boton2 = Button(raiz, bg="aqua", text="VACIAR",
                        command=vaciado, width=15)
        boton2.pack()
        boton2. place(x=380, y=170)

        """temp = uniform(0, 100)

        llenado1()
        time.sleep(0.5)

        if temp > 80:
            vaciado()
        else:
            llenado2()
            time.sleep(0.5)
            vaciado()"""


raiz = Tk()
raiz.geometry("500x300")
raiz.config(bg="black")
Caldera = Caldera(raiz)
raiz.mainloop()
