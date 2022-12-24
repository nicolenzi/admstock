import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql
from datetime import date
from datetime import datetime

fecha = datetime.now()

ventAñadir = tk.Tk()
ventAñadir.title("Añadir Stock")
ventAñadir.geometry("800x600")
ventAñadir.configure(bg="#AED6F1")


# SQL
sqlconex = sql.connect("admsBD.db")
curs = sqlconex.cursor()

# curs.execute('''INSERT INTO Mercaderia ("Tortas raspadas")VALUES (0)''')
# curs.execute('''INSERT INTO Mercaderia ("Medialunas")VALUES (0)''')


#           METODOS

#__

#           FRAMES
#   Frame Izquierdo
frameIzq = Frame(ventAñadir, bg="#85C1E9",width="100",height="580")
frameIzq.place(relx=0,rely=0)

#Labels
txtFrozen = Label(ventAñadir, text="Frozen",fg="white",bg="#85C1E9", font=("source",16))
txtFrozen.grid(row=0,column=0,padx=10)
#_

#Botones
btnVolver = Button(ventAñadir, text="Volver",fg="white",bg="#85C1E9", bd=0, width="8")
btnVolver.grid(row=1,column=0,pady=250)
#_


#   __

#   Frame centro
frameCent = Frame(ventAñadir, bg="white", width="740",height="580")
frameCent.place(relx=0.099,rely=0)

#Labels
txtAñadStk = Label(ventAñadir, text="Añadir stock",bg="white", font=("source",14))
txtAñadStk.place(relx=0.2,rely=0.1)

txtMercad = Label(ventAñadir, text="Mercaderia",bg="white", font=("courier",11))
txtMercad.place(relx=0.2,rely=0.2)

txtCant = Label(ventAñadir, text="Cantidad", bg="white", font=("courier",11))
txtCant.place(relx=0.45,rely=0.2)

#Botones

#Entrys
entryCant = Entry(ventAñadir,width="10")
entryCant.place(relx=0.54, rely=0.2)

#Comboboxs
comboMercad = ttk.Combobox(ventAñadir,state="readonly",width="10",values=["Medialunas","pinchadas","raspadas"])
comboMercad.place(relx=0.31,rely=0.2)
#_


#   __

#   Frame Inferior
frameInf = Frame(ventAñadir,bg="black",width="800",height="20")
frameInf.place(relx=0,rely=0.966)

#Labels



#_


#   __
#__

ventAñadir.mainloop()