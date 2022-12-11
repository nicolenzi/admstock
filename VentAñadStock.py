import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql
from datetime import date
from datetime import datetime

fecha = datetime.now()

ventanaPed = tk.Tk()
ventanaPed.title("Pedidos")
ventanaPed.geometry("800x600")
ventanaPed.configure(bg="#AED6F1")

#SQL
sqlconex = sql.connect("admsBD.db")
curs = sqlconex.cursor()

#curs.execute('''CREATE TABLE "Mercaderia" (
#	"Medialunas"	INTEGER,
#	"Tortas Pinchadas"	INTEGER
#)''')


#curs.execute('''INSERT INTO Mercaderia ("Tortas raspadas")VALUES (0)''')
#curs.execute('''INSERT INTO Mercaderia ("Medialunas")VALUES (0)''')

curs.execute('''SELECT * FROM stock''')
produc = curs.fetchall()
print(produc)


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

frameListP = Frame(frameCentro, width="800", height="200", bg="blue")
frameListP.place(relx=0.08, rely=0.6)

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

#Labels de frameList
txtNroFL = Label(frameListP, text="Nro", font=("Calabri", 12))
txtNroFL.grid(row=0,column=0, ipadx=10)

txtProducFL = Label(frameListP,text="Tipo mercaderia", font=("Calabri", 12))
txtProducFL.grid(row=0,column=1, ipadx=10)

txtCantFL = Label(frameListP,text="Cantidad total", font=("Calabri", 12))
txtCantFL.grid(row=0,column=2, ipadx=10)

txtFechaFL = Label(frameListP, text="Fecha actual", font=("Calabri", 12))
txtFechaFL.grid(row=0,column=3, ipadx=10)

txtUsrFL = Label(frameListP, text="Usuario", font=("Calabri", 12))
txtUsrFL.grid(row=0,column=4, ipadx=10)


#Combobox
ListaProd = ttk.Combobox(frameCentro,
            state="readonly",
            values=["Medialunas","Tortas pinchadas","Tortas raspadas"])
ListaProd.place(relx=0.2,rely=0.4)

#Entrys
entryCant = Entry(frameCentro,
            width="8")
entryCant.place(relx=0.6,rely=0.4)

#Metodos
def calculadora():
    print("calculadora!")
    calc = Toplevel()
    calc.title("calculadora")
    calc.geometry("400x400")

    carro=1960
    lata=49
    unidad=0

    #Labels
    txtCarros = Label(calc,text="Carros:")
    txtCarros.grid(row=0,column=0)

    txtLatas = Label(calc,text="Latas:")
    txtLatas.grid(row=1,column=0)

    txtUnid = Label(calc,text="Unidades:")
    txtUnid.grid(row=2,column=0)

    #Entrys
    entryCarro = Entry(calc)
    entryCarro.grid(row=0,column=1)

    entryLata = Entry(calc)
    entryLata.grid(row=1,column=1)

    entryUnid = Entry(calc)
    entryUnid.grid(row=2,column=1)

    def resultado(): #C = carro, L = lata, U = unidad
        C = int(entryCarro.get())
        L = int(entryLata.get())
        U = int(entryUnid.get())
        resulF = (C * carro + L * lata + U)
        messagebox.showinfo(message=resulF,title="Resultado final")
         

    
    #Botones
    btnconfirm = Button(calc,text="Comfirmar",command=resultado)
    btnconfirm.grid(row=3,column=1)

    calc.mainloop()

def Añadir():
    entCant = entryCant.get()

    curs.execute('''INSERT INTO Stock ("cantidad")VALUES ('{}')''')
    sqlconex.commit()
    sqlconex.close()

#Botones 
btnCalc = Button(frameCentro,
          text="Calculadora",
          command=calculadora)
btnCalc.place(relx=0.71,rely=0.4)

btnAñadir = Button(frameCentro, text="+", command=Añadir)
btnAñadir.place(relx=0.89,rely=0.4)



ventanaPed.mainloop()