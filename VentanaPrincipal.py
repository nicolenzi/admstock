import tkinter as tk
from tkinter import *
from tkinter import messagebox


ventanaP = tk.Tk()
ventanaP.title("Ventana principal")
ventanaP.geometry("800x600")
ventanaP.configure(bg = "#AED6F1")

#Frames
frameUrsInfo = Frame(ventanaP,
               width="800",
               height="30",
               bg="black")
frameUrsInfo.pack(side=BOTTOM)

frameOpc = Frame(ventanaP,
           width="90",
           height="570",
           bg="#85C1E9")
frameOpc.pack(side=LEFT)

frameCentro = Frame(ventanaP,
              width="750",
              height="570",
              bg="snow")
frameCentro.pack(side=LEFT)

#Labels
txtFrozen = Label(frameOpc,
            text="FROZEN",
            bg ="#85C1E9",
            width="10",
            height="2",
            font=("arial",12))
txtFrozen.place(relx=0,rely=0)

txtAñadirS = Label(frameCentro,
             text="Añadir stock",
             bg="white")
txtAñadirS.place(relx=0.22,rely=0.25)

txtListado = Label(frameCentro,
             text="Listado de stock",
             bg="white")
txtListado.place(relx=0.5,rely=0.25)

txtUsr = Label(frameUrsInfo,
         text="Usuario: ")
txtUsr.place(relx=0.7,rely=0)

#Botones
btnconfig = Button(frameOpc,
            text="Ajustes",
            width="8",
            bg="#85C1E9")
btnconfig.place(relx=0,rely=0.4)

btnañadir = Button(frameCentro,
            text="+",
            width="12",
            height="10")
btnañadir.place(relx=0.2, rely=0.3)

btnListado = Button(frameCentro,
             text="____",
             width="12",
             height="10")
btnListado.place(relx=0.5, rely=0.3)


ventanaP.mainloop()