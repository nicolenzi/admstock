import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from datetime import date
from datetime import datetime

fecha = datetime.now()

ventanaPed = tk.Tk()
ventanaPed.title("Pedidos")
ventanaPed.geometry("800x600")
ventanaPed.configure(bg="#AED6F1")

#frames


frameOpc = Frame(ventanaPed,
           width="90",
           height="600",
           bg="#85C1E9")
frameOpc.pack(side=LEFT)

frameCentro = Frame(ventanaPed,
           width="710",
           height="600",
           bg="orange")
frameCentro.pack(side=LEFT)

#Labels
txtFecha = Label(frameCentro,
           text="fecha: ",
           bg="snow")
txtFecha.place(relx=0.1,rely=0.3)

txtFechaAct = Label(frameCentro,
              text=fecha)
txtFechaAct.place(relx=0.2,rely=0.3)

txtNomUsr = Label(frameCentro,
         text="Usuario: ")
txtNomUsr.place(relx=0.6,rely=0.3)

txtNomUsrAct = Label(frameCentro,
               text="usr",
               bg="white")
txtNomUsrAct.place(relx=0.7,rely=0.3)

txtProd = Label(frameCentro,
          text="Producto:")
txtProd.place(relx=0.1,rely=0.4)

txtCant = Label(frameCentro,
          text="Cantidad:")
txtCant.place(relx=0.5,rely=0.4)

txtPedRec = Label(frameCentro,
            text="Pedidos realizados recientemente:")
txtPedRec.place(relx=0.1,rely=0.6)

#Combobox
ListaProd = ttk.Combobox(frameCentro,
            state="readonly",
            values=["Medialunas","Tortas pinchadas","Tortas raspadas"])
ListaProd.place(relx=0.2,rely=0.4)

#Entrys
entryCant = Entry(frameCentro,
            width="8")
entryCant.place(relx=0.6,rely=0.4)

#Botones 
btnAñadir = Button(frameCentro, text="+")
btnAñadir.place(relx=0.89,rely=0.4)

btnCalc = Button(frameCentro,
          text="Calculadora")
btnCalc.place(relx=0.71,rely=0.4)



ventanaPed.mainloop()