import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql


ventanaP = tk.Tk()
ventanaP.title("Ventana principal")
ventanaP.geometry("800x600")
ventanaP.configure(bg = "#AED6F1")

def abrirAñdStk():
    print("Añadir ventana")
def abrirListStk():
    print("Listado ventana")
#CONEXION A SQL
sqlconex = sql.connect("Usuarios")
curs = sqlconex.cursor()

UsrAct = "Predeterminado"


#Frames
frameUrsInfo = Frame(ventanaP,
               width="800",
               height="30",
               bg="black")
frameUrsInfo.pack(side=BOTTOM)

frameOpc = Frame(ventanaP,
           width="110",
           height="570",
           bg="#EBF5FB")
frameOpc.pack(side=LEFT)

frameCentro = Frame(ventanaP,
              width="750",
              height="570",
              bg="white")
frameCentro.pack(side=LEFT)

#txt
imgFrzn = PhotoImage(file="imagenes/titulo.png")
imgFrozen = Label(frameOpc,image=imgFrzn,width="110",height="50")
imgFrozen.place(relx=0,rely=0)

txtAnadirS = Label(frameCentro,
             text="Añadir stock",
             bg="white",font=("courier",10))
txtAnadirS.place(relx=0.22,rely=0.25)

txtListado = Label(frameCentro,
             text="Listado de stock",
             bg="white",font=("courier",10))
txtListado.place(relx=0.57,rely=0.25)

txtUsr = Label(frameUrsInfo,font=("courier",9),
         text="Usuario: "+UsrAct,fg="white",bg="black")
txtUsr.place(relx=0.75,rely=0.1)

#Botones

btnSalir = Button(frameOpc,
            text="Salir",
            font=("courier",10),
            fg="white",
            bd=0,
            width="13",
            height="1",
            bg="red")
btnSalir.place(relx=0,rely=0.96)

#imagenes
imgAS = PhotoImage(file="imagenes/añadirS.png")
#lbimg = Label(frameCentro, image = imgAS)

imgLS = PhotoImage(file="imagenes/listadoS.png")
#lbimg2 = Label(frameCentro, image= imgLS)

btañadir = Button(frameCentro,image=imgAS,
            text="+",
            width="95",
            height="125",
            bd=0,
            bg="white",
            command=abrirAñdStk)
btañadir.place(relx=0.23, rely=0.35)

btnListado = Button(frameCentro,image=imgLS,
             width="113",
             bd=0,
             height="143",
             command=abrirListStk)
btnListado.place(relx=0.6, rely=0.35)


ventanaP.mainloop()
sqlconex.close()