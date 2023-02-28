

"""
import tkinter as tk
from tkinter import *
import sqlite3 as sql

ventana = tk.Tk()

sqlconex = sql.connect("Basedatos_prueba.db")
curs = sqlconex.cursor()

def Añadir():
    entrVal = entryValor.get()     #añadir a BD el valor del entry
                                                             #v
    curs.execute('''INSERT INTO Ejemplo ("Lugar") VALUES (?)''',entrVal)
    sqlconex.commit()

def Buscar():
    
    busqueda = entryBusqueda.get()

    curs.execute("SELECT * FROM Ejemplo WHERE Lugar = ? ",busqueda)
    sqlconex.commit()
    datos = curs.fetchall()

    print(datos)
    txtEjemp.configure(text=datos)
   # for dato in datos:
   #     print(dato)
   

def Copiar():
    lista.insert(1,)  #devolver un valor?? --- con lo que se añade en la base de datos copiarlo al listbox(si total es temporal)


entryValor = Entry(ventana)
entryValor.grid(row=0,column=0)

entryBusqueda = Entry(ventana)
entryBusqueda.grid(row=2,column=0)

txtEjemp = Label(ventana,text="ejemplo")
txtEjemp.grid(row=1,column=0)

lista = Listbox(ventana)
lista.grid(row=3,column=0)



btnAñadir = Button(ventana, text="Añadir a BD", command=Añadir)
btnAñadir.grid(row=0,column=1)

btnbuscar = Button(ventana, text="Buscar",command=Buscar)
btnbuscar.grid(row=2,column=1)

ventana.mainloop()
sqlconex.close()
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
"""

'''
import tkinter as tk
from tkinter import *
import sqlite3 as sql

ventana = tk.Tk()
ventana.geometry("400x400")
sqlconex = sql.connect("Basedatos_prueba.db")
curs = sqlconex.cursor()

listboxx = Listbox(ventana)
listboxx.pack()
curs.execute("SELECT * FROM Ejemplo")
listado = curs.fetchall()

inicio = 0

for lista in listado:
    listboxx.insert(inicio,listado[5])
    inicio = inicio + 1

ventana.mainloop()
sqlconex.close()
'''
'''
import tkinter as tk
from tkinter import *
from tkinter import IntVar

ventana = tk.Tk()
ventana.geometry("400x400")

CVar = IntVar()
CVar2 = IntVar()

def ver():
    lbel.configure(text=CVar.get())
    print(CVar.get())

        


lbel = Label(ventana,text="")
lbel.pack()

check = Checkbutton(ventana,text="valor1",variable=CVar,onvalue=2,offvalue=0)
check.pack()

check2 = Checkbutton(ventana,text="",variable=CVar2)


Btn = Button(ventana,text="probar",command=ver)
Btn.pack()



ventana.mainloop()
'''
