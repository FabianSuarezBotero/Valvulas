import tkinter as tk
import time
class CanvasTanque(tk.Canvas):
    
    def __init__(self, frame=None,type="a" , color="blue"):
        self.color=color
        self.type=type
        self.estado = True
        super().__init__(frame, width = 200, height = 180, bg = 'grey', highlightthickness=0)
        self.crear()
        
    def crear(self):
        #tanque = tk.Canvas(self, width = 200, height = 180, bg = 'black', highlightthickness=0) 
        self.columnconfigure(1,weight=1)
        self.place(x=70, y=1)
        
        self.create_rectangle(140,20,10,150, fill= "#CAC6BE") #tanque vacio 
        self.create_oval(10,130,140,160, fill= "#CAC6BE") #tapa inferior tanque vacio
        
        self.create_rectangle(140,40,10,150, fill= self.color) #tanque liquido 
        self.create_oval(10,130,140,160, fill= self.color) #tapa inferior tanque liquido
        self.create_oval(10,30,140,60, fill= self.color) #tapa superior tanque liquido
        
        self.create_oval(10,10,140,40, fill= "#CAC6BE") #tapa superior tanque vacio
        self.create_polygon(140,10,200,10,180,30,180,50,160,50,160,30, fill="red") #Tolva/valvula
        
        if(self.type=="b"):
            self.create_polygon(140,70,200,70,180,90,180,110,160,110,160,90, fill="red")
      
    def estadoTanque(self):
        a=self.estado
        return a
    
    def llenar(self):
        num = 149
        
        if(self.estado == False):
            if(self.type=="a"):
                self.create_polygon(140,10,200,10,180,30,180,50,160,50,160,30, fill="red")
            elif(self.type=="b"):
                self.create_polygon(140,10,200,10,180,30,180,50,160,50,160,30, fill="green")    
            
            for i in range(40, num):
                self.create_rectangle(140, 20, 10, 150, fill="#CAC6BE")
            
                self.create_oval(10,130,140,160, fill= self.color)
                self.create_rectangle(10, num, 140, 150, fill= self.color)
                self.create_oval(10,num-15,140,num+15, fill= self.color) #tapa superior tanque liquido
            
                self.create_oval(10,10,140,40, fill= "#CAC6BE") #tapa superior tanque vacio
                self.update()

                time.sleep(0.015)
                num = num - 1
                #N = int((i-64)*250)
            
            if(self.type=="b"):
                 
                self.create_polygon(140,10,200,10,180,30,180,50,160,50,160,30, fill="red")
            if(self.type=="a"):
                self.create_polygon(140,10,200,10,180,30,180,50,160,50,160,30, fill="red")    
            
            self.create_oval(10,130,140,160, fill= self.color) #tapa inferior tanque liquido
            self.estado=1
            
    def vaciado(self):
        if(self.estado==True):
            if(self.type=="a"):
                self.create_polygon(140,10,200,10,180,30,180,50,160,50,160,30, fill="green")
            elif(self.type=="b"):
                self.create_polygon(140,70,200,70,180,90,180,110,160,110,160,90, fill="green")
                
            for a in range(40, 149):
                self.create_rectangle(140, 20, 10, 150, fill="#CAC6BE")
            
                self.create_oval(10,130,140,160, fill= self.color)
                self.create_rectangle(10, a, 140, 150, fill=self.color)
                self.create_oval(10,a-15,140,a+15, fill= self.color) #tapa superior tanque liquido
            
                self.create_oval(10,10,140,40, fill= "#CAC6BE") #tapa superior tanque vacio
                self.update()

                time.sleep(0.015)
                #l = int(25000 - (a-64)*250)
            self.create_oval(10,130,140,160, fill= "#CAC6BE") #tapa inferior tanque vacio
            
            if(self.type=="a"):
                self.create_polygon(140,10,200,10,180,30,180,50,160,50,160,30, fill="red")
            elif(self.type=="b"):
                self.create_polygon(140,70,200,70,180,90,180,110,160,110,160,90, fill="red")
            
            self.estado=0

    
        
####### :v

class TanqueCont(tk.LabelFrame):
    #prueba= 1
    def __init__(self, pantalla=None,typeTanque="a",colorTanque="blue"):
        super().__init__(pantalla,width= 400, height= 200, text="Tanque", bg= "grey")
        self.pack()
        self.tanque= CanvasTanque(self,color=colorTanque,type=typeTanque)
        self.crear()
        
        
    def estado(self):
        a=self.tanque.estadoTanque()    
        return a

         
        
        
        
    def crear(self):
        #print(self.prueba)
        maximo=100
        max = tk.Label(self, text= "max "+str(maximo)+"➡", bg= "white", fg= "black", font= "Helvetica 10 bold")
        max.place(y=30,x=1)
        minimo= "0"
        min = tk.Label(self, text= "min "+"0"+"➡", bg= "white", fg= "black", font= "Helvetica 10 bold")
        min.place(y=130,x=1)
        
        
        
        
        boton = tk.Button(self, bg="magenta", text="LLENAR1", width=15)
        boton.pack()
        boton.place(x=280, y=80)
        
        boton2 = tk.Button(self, bg="aqua", text="VACIAR", width=15)
        boton2.pack()
        boton2.place(x=280, y=130) 
        boton2.configure(command= lambda: self.tanque.vaciado()) 
        boton.configure(command= lambda: self.tanque.llenar())
    
    def vaciar(self):
        self.tanque.vaciado()
               
    def llenar(self):
        self.tanque.llenar()    
        
        
        
    #def llenar(self):
     #   num=165
      #  for i in range(55, num):
       #     tanque.create_rectangle(140,num,10,150, fill= "blue") #tanque liquido 
        #    tanque.udpade


        
#raiz= tk.Tk()
#raiz.geometry("500x300")
#tanque1= TanqueCont(raiz,typeTanque="a",colorTanque="black")
#raiz.config(bg="black")
#tanque1.llenar() 
#tanque1.vaciar()
#print(str(tanque1.estado()))

#raiz.mainloop()       