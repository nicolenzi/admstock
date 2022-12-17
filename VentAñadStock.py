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

# SQL
sqlconex = sql.connect("admsBD.db")
curs = sqlconex.cursor()

# curs.execute('''CREATE TABLE "Mercaderia" (
#	"Medialunas"	INTEGER,
#	"Tortas Pinchadas"	INTEGER
# )''')


# curs.execute('''INSERT INTO Mercaderia ("Tortas raspadas")VALUES (0)''')
# curs.execute('''INSERT INTO Mercaderia ("Medialunas")VALUES (0)''')



# frames


frameOpc = Frame(ventanaPed, width="90", height="600", bg="#A9CCE3")
frameOpc.pack(side=LEFT)

# FRAME CENTRO
frameCentro = Frame(ventanaPed, width="710", height="600", bg="#85C1E9")
frameCentro.pack(side=LEFT)

# Labels (FC)

txtFecha = Label(frameCentro, text="fecha: ", bg="#85C1E9")
txtFecha.place(relx=0.05, rely=0.1)

txtFechaAct = Label(frameCentro, text=fecha, bg="#85C1E9")
txtFechaAct.place(relx=0.13, rely=0.1)

txtNomUsr = Label(frameCentro, text="Usuario: ", bg="#85C1E9")
txtNomUsr.place(relx=0.4, rely=0.1)

txtNomUsrAct = Label(frameCentro, text="ADM", bg="#85C1E9")
txtNomUsrAct.place(relx=0.5, rely=0.1)

txtProd = Label(frameCentro, text="Producto:", bg="#85C1E9")
txtProd.place(relx=0.05, rely=0.25)

txtCant = Label(frameCentro, text="Cantidad:", bg="#85C1E9")
txtCant.place(relx=0.4, rely=0.25)

txtFecha = Label(frameCentro, text="Fecha:", bg="#85C1E9")
txtFecha.place(relx=0.05, rely=0.35)

txtNomUsr1 = Label(frameCentro, text="Usuario:", bg="#85C1E9")
txtNomUsr1.place(relx=0.37, rely=0.35)

# Botones (FC)


# Combobox (FC)

ListaProd = ttk.Combobox(frameCentro, state="readonly", values=["Medialunas", "Tortas pinchadas", "Tortas raspadas"])
ListaProd.place(relx=0.15, rely=0.25)

frameListP = Frame(frameCentro, width="800", height="200", bg="blue")
frameListP.place(relx=0.045, rely=0.6)

# Entrys (FC)


# Labels
txtFrozen = Label(frameOpc, text="Frozen", font=("source", 15), fg="white", bg="#A9CCE3")
txtFrozen.place(relx=0.1, rely=0)

# Labels de frameList
txtNroFL = Label(frameListP, text="Nro", bg="#5DADE2", font=("Calabri", 12))
txtNroFL.grid(row=0, column=0, ipadx=10)

txtProducFL = Label(frameListP, text="Tipo mercaderia", bg="#5DADE2", font=("Calabri", 12))
txtProducFL.grid(row=0, column=1, ipadx=10)

txtCantFL = Label(frameListP, text="Cantidad total", bg="#5DADE2", font=("Calabri", 12))
txtCantFL.grid(row=0, column=2, ipadx=10)

txtFechaFL = Label(frameListP, text="Fecha actual", bg="#5DADE2", font=("Calabri", 12))
txtFechaFL.grid(row=0, column=3, ipadx=10)

txtUsrFL = Label(frameListP, text="Usuario", bg="#5DADE2", font=("Calabri", 12))
txtUsrFL.grid(row=0, column=4, ipadx=10)

# Entrys
entryCant = Entry(frameCentro, width="8")
entryCant.place(relx=0.5, rely=0.25)

entryFecha = Entry(frameCentro, width="15")
entryFecha.place(relx=0.12, rely=0.35)

entryUsr = Entry(frameCentro, width="15")
entryUsr.place(relx=0.45, rely=0.35)


# Metodos
def calculadora():
    print("calculadora!")
    calc = Toplevel()
    calc.title("calculadora")
    calc.geometry("250x100")

    carro = 1960
    lata = 49
    unidad = 0

    # Labels
    txtCarros = Label(calc, text="Carros:")
    txtCarros.grid(row=0, column=0)

    txtLatas = Label(calc, text="Latas:")
    txtLatas.grid(row=1, column=0)

    txtUnid = Label(calc, text="Unidades:")
    txtUnid.grid(row=2, column=0)

    # Entrys
    entryCarro = Entry(calc)
    entryCarro.grid(row=0, column=1)

    entryLata = Entry(calc)
    entryLata.grid(row=1, column=1)

    entryUnid = Entry(calc)
    entryUnid.grid(row=2, column=1)

    def resultado():  # C = carro, L = lata, U = unidad
        C = int(entryCarro.get())
        L = int(entryLata.get())
        U = int(entryUnid.get())
        resulF = (C * carro + L * lata + U)
        messagebox.showinfo(message=resulF, title="Resultado final")

    # Botones
    btnconfirm = Button(calc, text="Comfirmar", command=resultado)
    btnconfirm.grid(row=3, column=1)

    calc.mainloop()


def Añadir():
    total = (entryCant.get(), ListaProd.get(), entryUsr.get(), entryFecha.get())

    curs.execute("INSERT INTO Stock(Cantidad,Producto,Usuario,Fecha) VALUES(?,?,?,?)", total)
    datosAnadir = curs.fetchall()
    sqlconex.commit()
    sqlconex.close()
    print("añadido exitosamente")


# Botones

# prob con metodo
btnAjustes = Button(frameOpc, text="Ajustes", bg="#AED6F1", bd=0, width=10)
btnAjustes.place(relx=0, rely=0.2)

btnSalir = Button(frameOpc, text="Salir", bg="#154360", bd=0, width=10)
btnSalir.place(relx=0, rely=0.95)


def Consulta():
    curs = sqlconex.cursor()


btnBuscar = Button(frameCentro, text="Buscar", command=Consulta, bg="#3498DB", bd=0)
btnBuscar.place(relx=0.8, rely=0.7, width=85)

btnActualizar = Button(frameCentro, text="Actualizar", bg="#3498DB", bd=0)
btnActualizar.place(relx=0.8, rely=0.76)

btnEliminar = Button(frameCentro, text="Eliminar", width=8, bg="#3498DB", bd=0)
btnEliminar.place(relx=0.8, rely=0.82)

# listbox
stocks = Listbox(width="75", fg="red")

stocks.place(relx=0.15, rely=0.65)

ventanaPed.mainloop()