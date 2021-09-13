from tkinter import *
import time
from random import *
import tkinter as tk


class Fogon(tk.LabelFrame):

    def __init__(self, pantalla=None):

        super().__init__(pantalla)
        self.estado = 0
        self.grados = 25

        self.config(width=600, height=200,
                    bg="blue", highlightthickness=0)
        self.pack(padx=10, pady=10)

        self.caldera = Canvas(self, width=800, height=200, bg='grey')
        self.caldera.place(x=100, y=100)

        self.caldera.create_rectangle(140, 30, 320, 165, fill="#CAC6BE")

        self.caldera.create_oval(140, 155, 320, 175, fill="#CAC6BE")
        self.caldera.create_oval(140, 15, 320, 45, fill="#CAC6BE")

        self.caldera.create_polygon(100, 140, 70, 185, 130, 185, fill='white')
        self.caldera.create_polygon(100, 85, 70, 130, 130, 130, fill='white')
        self.caldera.create_polygon(100, 30, 70, 75, 130, 75, fill='white')

        nombre1 = Label(self, text="Nivel 2", bg="black",
                        fg="white", font="Helvetica 12 bold")
        nombre1.pack()
        nombre1.place(x=335, y=42)

        nombre2 = Label(self, text="Nivel 1", bg="black",
                        fg="white", font="Helvetica 12 bold")
        nombre2.pack()
        nombre2.place(x=335, y=95)
        self.crear()

    def llenado1(self):
        num = 149
        for i in range(110, num):
            self.caldera.create_rectangle(140, 30, 320, 165, fill="#CAC6BE")
            self.caldera.create_oval(140, 150, 320, 170, fill="pink")
            self.caldera.create_rectangle(140, num, 320, 165, fill="pink")
            self.caldera.create_oval(140, 155, 320, 175, fill="pink")
            # tapa superior tanque liquido
            self.caldera.create_oval(140, num-15, 320, num+15, fill="pink")

            # tapa superior tanque vacio
            self.caldera.create_oval(140, 15, 320, 45, fill="#CAC6BE")
            self.caldera.update()

            time. sleep(0.01)
            num = num - 1
            N = int((i-64)*250)

            self.estado = 1

    def mostrar_estado(self):
        return self.estado

    def mostrar_temp(self):
        return self.temperatura

    def llenado2(self):
        while self.estado == 1:
            num = 110
            for i in range(55, num):
                self.caldera.create_rectangle(
                    140, 30, 320, 165, fill="#CAC6BE")
                self.caldera.create_oval(140, 150, 320, 170, fill="pink")
                self.caldera.create_rectangle(140, num, 320, 165, fill="pink")
                self.caldera.create_oval(140, 155, 320, 175, fill="pink")
                # tapa superior tanque liquido
                self.caldera.create_oval(140, num-15, 320, num+15, fill="pink")

                # tapa superior tanque vacio
                self.caldera.create_oval(140, 15, 320, 45, fill="#CAC6BE")
                self.caldera.update()

                time. sleep(0.01)
                num = num - 1
                N = int((i-64)*250)

                self.estado = 2

    def vaciado2(self):
        while self.estado == 2:

            for a in range(55, 165):
                self.caldera.create_rectangle(
                    140, 30, 320, 165, fill="#CAC6BE")
                self.caldera.create_oval(140, 150, 320, 170, fill="pink")
                self.caldera.create_rectangle(140, a, 320, 165, fill="pink")
                self.caldera.create_oval(140, 155, 320, 175, fill="pink")
                # tapa superior tanque liquido
                self.caldera.create_oval(140, a-15, 320, a+15, fill="pink")

                # tapa superior tanque vacio
                self.caldera.create_oval(140, 15, 320, 45, fill="#CAC6BE")

                self.caldera.update()

                time.sleep(0.01)
                l = int(25000 - (a-64)*250)

                self.estado = 0

    def vaciado1(self):
        while self.estado == 1:

            for a in range(110, 165):
                self.caldera.create_rectangle(
                    140, 30, 320, 165, fill="#CAC6BE")
                self.caldera.create_oval(140, 150, 320, 170, fill="pink")
                self.caldera.create_rectangle(140, a, 320, 165, fill="pink")
                self.caldera.create_oval(140, 155, 320, 175, fill="pink")
                # tapa superior tanque liquido
                self.caldera.create_oval(140, a-15, 320, a+15, fill="pink")

                # tapa superior tanque vacio
                self.caldera.create_oval(140, 15, 320, 45, fill="#CAC6BE")

                self.caldera.update()

                time.sleep(0.01)
                l = int(25000 - (a-64)*250)

                self.estado = 0

    def subir_temperatura(self):
        if self.grados < 100 and self.grados >= 75:
            self.caldera.create_polygon(100, 30, 70, 75, 130, 75, fill='red')
            self.caldera.create_polygon(
                100, 140, 70, 185, 130, 185, fill='yellow')
            self.caldera.create_polygon(
                100, 85, 70, 130, 130, 130, fill='orange')
            self.grados = 100

        elif self.grados < 75 and self.grados >= 50:
            self.caldera.create_polygon(
                100, 85, 70, 130, 130, 130, fill='orange')
            self.caldera.create_polygon(
                100, 140, 70, 185, 130, 185, fill='yellow')
            self.caldera.create_polygon(100, 30, 70, 75, 130, 75, fill='white')
            self.grados = 75

        elif self.grados < 50:
            self.caldera.create_polygon(
                100, 140, 70, 185, 130, 185, fill='yellow')
            self.caldera.create_polygon(
                100, 85, 70, 130, 130, 130, fill='white')
            self.caldera.create_polygon(100, 30, 70, 75, 130, 75, fill='white')
            self.grados = 50
        return self.grados
        print(self.grados)

    def bajar_temperatura(self):
        if self.grados >= 50 and self.grados < 75:
            self.caldera.create_polygon(
                100, 140, 70, 185, 130, 185, fill='white')
            self.caldera.create_polygon(
                100, 85, 70, 130, 130, 130, fill='white')
            self.caldera.create_polygon(100, 30, 70, 75, 130, 75, fill='white')
            self.grados = 25

        elif self.grados >= 75 and self.grados < 100:
            self.caldera.create_polygon(
                100, 85, 70, 130, 130, 130, fill='white')
            self.caldera.create_polygon(
                100, 140, 70, 185, 130, 185, fill='yellow')
            self.caldera.create_polygon(100, 30, 70, 75, 130, 75, fill='white')
            self.grados = 50

        elif self.grados >= 100:
            self.caldera.create_polygon(100, 30, 70, 75, 130, 75, fill='white')
            self.caldera.create_polygon(
                100, 140, 70, 185, 130, 185, fill='yellow')
            self.caldera.create_polygon(
                100, 85, 70, 130, 130, 130, fill='orange')
            self.grados = 75
        return self.grados
        print(self.grados)

    def crear(self):
        self.caldera.pack()

        boton = Button(self, bg="magenta", text="LLENAR1",
                       command=self.llenado1, width=15)
        boton.pack()
        boton. place(x=380, y=120)

        boton3 = Button(self, bg="magenta", text="LLENAR2",
                        command=self.llenado2, width=15)
        boton3.pack()
        boton3. place(x=380, y=80)

        boton2 = Button(self, bg="aqua", text="VACIAR TODO",
                        command=self.vaciado2)
        boton2.pack()
        boton2. place(x=380, y=10)

        boton1 = Button(self, bg="aqua", text="VACIAR 1",
                        command=self.vaciado1)
        boton1.pack()
        boton1. place(x=380, y=40)

        boton4 = Button(self, bg="aqua", text="Subir temp",
                        command=self.subir_temperatura)
        boton4.pack()
        boton4. place(x=20, y=120)

        boton5 = Button(self, bg="aqua", text="Bajar temp",
                        command=self.bajar_temperatura)
        boton5.pack()
        boton5. place(x=20, y=170)


raiz = Tk()
raiz.geometry("500x300")
raiz.config(bg="black")
Caldera = Fogon(raiz)
raiz.mainloop()
