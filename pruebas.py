

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
"""
def valores():
    valor1 = 1
    valor2 = 2
    result = valor1 + valor1
    return result

suma_valor = valores()

print(suma_valor)
"""

"""
def argumentos(arg1,arg2):
    return arg1 + arg2

print("ingrese valor 1")
valor1 = input()

print("ingrese valor 2")
valor2 = input()

total = argumentos(valor1,valor2)
print(total)
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk

vent = tk.Tk()
vent.geometry("600x600")

valoringresado = "0" 
def copiarc():
   valoringresado = cbp.get()
   lap.configure(text="valor "+ valoringresado)
   print(valoringresado)

cbp = ttk.Combobox(vent,values=["uno","dos","tres"],state="readonly")
cbp.grid(row=0,column=0)

btnp = Button(vent,text="copiar",command=copiarc)
btnp.grid(row=0,column=1)

lap = Label(vent,text="valor "+valoringresado)
lap.grid(row=0,column=3)


vent.mainloop()