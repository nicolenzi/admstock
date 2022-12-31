
import tkinter as tk
from tkinter import *

ventana = tk.Tk()
ventana.geometry("600x600")
activar = NORMAL

def act():
    activar=ACTIVE

btn1 = Button(ventana, text="b1",command=act)
btn1.place(relx=0.2,rely=0.2)

btn2 = Button(ventana, text="b2",state=DISABLED)
btn2.place(relx=0.3, rely=0.2)

ventana.mainloop()






"""
import tkinter as tk
from tkinter import *
import sqlite3 as sql

ventana = tk.Tk()

sqlconex = sql.connect("BaseDatos.db")
curs = sqlconex.cursor()


entryValor = Entry(ventana)
entryValor.grid(row=0,column=0)



def Añadir():
    entrVal = entryValor.get()     #añadir a BD el valor del entry
                                                             #v
    curs.execute('''INSERT INTO Ejemplo ("Casilla 1") VALUES (?)''')
    sqlconex.commit()
    sqlconex.close()


btnAñadir = Button(ventana, text="Añadir a BD", command=Añadir)
btnAñadir.grid(row=0,column=1)

ventana.mainloop()
"""