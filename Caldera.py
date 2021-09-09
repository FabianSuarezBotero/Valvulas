from tkinter import *
import time
from random import *


class Caldera():
    estado = 0
    temperatura = 0

    def __init__(self, pantalla):
        frame = Frame(pantalla)
        frame.config(width=800, height=200, bg="blue", highlightthickness=0)
        frame.pack(padx=10, pady=10)

        self.caldera = Canvas(frame, width=800, height=200, bg='grey')
        self.caldera.place(x=100, y=100)

        self.caldera.create_rectangle(140, 30, 320, 165, fill="#CAC6BE")

        self.caldera.create_oval(140, 155, 320, 175, fill="#CAC6BE")
        self.caldera.create_oval(140, 15, 320, 45, fill="#CAC6BE")

        self.caldera.create_polygon(100, 140, 70, 185, 130, 185, fill='white')
        self.caldera.create_polygon(100, 85, 70, 130, 130, 130, fill='white')
        self.caldera.create_polygon(100, 30, 70, 75, 130, 75, fill='white')

        nombre1 = Label(raiz, text="Nivel 2", bg="black",
                        fg="white", font="Helvetica 12 bold")
        nombre1.pack()
        nombre1.place(x=335, y=50)

        nombre2 = Label(raiz, text="Nivel 1", bg="black",
                        fg="white", font="Helvetica 12 bold")
        nombre2.pack()
        nombre2.place(x=335, y=110)
        self.crear()

    def llenado1(self):
        num = 149
        for i in range(110, num):
            self.caldera.create_rectangle(140, 30, 320, 165, fill="#CAC6BE")
            self.caldera.create_oval(140, 150, 320, 170, fill="blue")
            self.caldera.create_rectangle(140, num, 320, 165, fill="blue")
            self.caldera.create_oval(140, 155, 320, 175, fill="blue")
            # tapa superior tanque liquido
            self.caldera.create_oval(140, num-15, 320, num+15, fill="blue")

            # tapa superior tanque vacio
            self.caldera.create_oval(140, 15, 320, 45, fill="#CAC6BE")
            self.caldera.update()

            time. sleep(0.01)
            num = num - 1
            N = int((i-64)*250)

            estado = 1

    def llenado2(self):
        num = 119
        for i in range(55, num):
            self.caldera.create_rectangle(140, 30, 320, 165, fill="#CAC6BE")
            self.caldera.create_oval(140, 150, 320, 170, fill="blue")
            self.caldera.create_rectangle(140, num, 320, 165, fill="blue")
            self.caldera.create_oval(140, 155, 320, 175, fill="blue")
            # tapa superior tanque liquido
            self.caldera.create_oval(140, num-15, 320, num+15, fill="blue")

            # tapa superior tanque vacio
            self.caldera.create_oval(140, 15, 320, 45, fill="#CAC6BE")
            self.caldera.update()

            time. sleep(0.01)
            num = num - 1
            N = int((i-64)*250)

            estado = 2

    def vaciado(self):
        for a in range(55, 165):
            self.caldera.create_rectangle(140, 30, 320, 165, fill="#CAC6BE")
            self.caldera.create_oval(140, 150, 320, 170, fill="blue")
            self.caldera.create_rectangle(140, a, 320, 165, fill="blue")
            self.caldera.create_oval(140, 155, 320, 175, fill="blue")
            # tapa superior tanque liquido
            self.caldera.create_oval(140, a-15, 320, a+15, fill="blue")

            # tapa superior tanque vacio
            self.caldera.create_oval(140, 15, 320, 45, fill="#CAC6BE")

            self.caldera.update()

            time.sleep(0.015)
            l = int(25000 - (a-64)*250)

            estado = 0

    def subir_temperatura(self):
        if temperatura == 0:

    def crear(self):
        self.caldera.pack()

        boton = Button(raiz, bg="magenta", text="LLENAR1",
                       command=self.llenado1, width=15)
        boton.pack()
        boton. place(x=380, y=120)

        boton3 = Button(raiz, bg="magenta", text="LLENAR2",
                        command=self.llenado2, width=15)
        boton3.pack()
        boton3. place(x=380, y=80)

        boton2 = Button(raiz, bg="aqua", text="VACIAR",
                        command=self.vaciado, width=15)
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
