import tkinter as tk
from tkinter import *
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
           bg="red")
frameCentro.pack(side=LEFT)

#Labels
txtFecha = Label(frameCentro,
           text="fecha",
           bg="snow")
txtFecha.grid(row=0,column=0)

txtFechaAct = Label(frameCentro,
              text=fecha)
txtFechaAct.grid(row=0,column=1)

txtNom = Label(frameCentro,
         text="Usuario")
txtNom.grid(row=0,column=2)






ventanaPed.mainloop()