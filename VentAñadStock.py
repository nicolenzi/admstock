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

val_resulCalc = 0

# SQL
sqlconex = sql.connect("admsBD.db")
curs = sqlconex.cursor()

# curs.execute('''INSERT INTO Mercaderia ("Tortas raspadas")VALUES (0)''')
# curs.execute('''INSERT INTO Mercaderia ("Medialunas")VALUES (0)''')


#           METODOS

#__

#           FRAMES
#   Frame Izquierdo
frameIzq = Frame(ventAñadir, bg="#85C1E9",width="160",height="580")
frameIzq.place(relx=0,rely=0)

#Labels
txtFrozen = Label(ventAñadir, text="Frozen",fg="white",bg="#85C1E9", font=("source",16))
txtFrozen.grid(row=0,column=0,padx=10)
#_

#Botones
btnVolver = Button(ventAñadir, text="Volver",fg="white",bg="#85C1E9", bd=0, width="8")
btnVolver.grid(row=1,column=0,pady=250)
#_

def calcu():
    ventcal = Toplevel()
    ventcal.geometry("250x200")
    
    
    #Valores 
    

    #Medialunas50g
    mCarroC = 30
    mCarroG = 40
    mLata = 49
    

    #Medialunas60g
    mgCarroC = 30
    mgCarroG = 40
    mgLata = 42
    

    #Tortas pinchadas
    tpCarroC = 30
    tpCarroG = 40
    tpLata = 36
    

    #Tortas raspadas
    trCarroC = 30
    trCarroG = 40
    trLata = 36
    

    #Metodos
    def calculo():
        EC = int(entryCarro.get()) 
        EL = int(entryLata.get())
        EU = int(entryUnidad.get())
        
        if combo_produc.get() == "":
            print("No producto")
        elif combo_produc.get() == "Medialuna":  
            val_resulCalc = ((EC*mCarroG) * (EL*mLata) + EU)  # (ingreso de valor * cantidad de LATAS de carro de facturas)*(ingreso de valor * cantidad de UNIDADES de una lata de facturas) + unidades 
            txtTotal.configure(text="total: "+ str(val_resulCalc)) 
            print(val_resulCalc)

        elif combo_produc.get() == "Medialuna 60g":
            val_resulCalc = ((EC * mgCarroG) * (EL*mgLata) + EU)
            txtTotal.configure(text="Total: "+ str(val_resulCalc))
            print(val_resulCalc)

        elif combo_produc.get() == "Pinchadas":
            val_resulCalc = ((EC * tpCarroC) * (EL * tpLata) + EU)
            txtTotal.configure(text="Total: "+str(val_resulCalc))
            print(val_resulCalc)
        else:
            print("ERROR!")

       

    #Labels
    txtIngrese = Label(ventcal,text="Ingrese cantidad")
    txtIngrese.grid(row=0,column=0,columnspan=2,ipady=8)
    
    txtCarros = Label(ventcal,text="Carros:")
    txtCarros.grid(row=1,column=0)

    txtLatas = Label(ventcal,text="Latas:")
    txtLatas.grid(row=2,column=0)

    txtUnidad = Label(ventcal,text="Unidades:")
    txtUnidad.grid(row=3,column=0)
    
    txtTipo = Label(ventcal, text="Tipo: ")
    txtTipo.grid(row=4,column=0,sticky=E,ipady=6)

    txtTotal = Label(ventcal,text="total: ")
    txtTotal.grid(row=6,column=2)



    #Comboboxs
    combo_produc = ttk.Combobox(ventcal,values=["Medialuna","Medialuna 60g","Pinchadas"],state="readonly")
    combo_produc.grid(row=4,column=1)
    #Entrys
    entryCarro = Entry(ventcal)         #si hay problemas con la suma string cambiar a int() O UNA ,
    entryCarro.grid(row=1,column=1)

    entryLata = Entry(ventcal)
    entryLata.grid(row=2,column=1)

    entryUnidad = Entry(ventcal)
    entryUnidad.grid(row=3,column=1)
    entryCarro.insert(0,0)
    entryLata.insert(0,0)
    entryUnidad.insert(0,0)

    #Botones
    btnCalcular = Button(ventcal,text="Calcular",command=calculo)
    btnCalcular.grid(row=6,column=1)
    


    ventcal.mainloop()
#   __

#   Frame centro
frameCent = Frame(ventAñadir, bg="white", width="740",height="580")
frameCent.place(relx=0.099,rely=0)

frameBg1 = Frame(frameCent, bg="#EBF5FB",width="600",height="150")
frameBg1.place(relx=0.05,rely=0.2)

frameBg2 = Frame(frameCent, bg="#D5F5E3",width="600",height="150")
frameBg2.place(relx=0.05,rely=0.6)

#Labels
txtAñadStk = Label(ventAñadir, text="Añadir stock",bg="#EBF5FB", font=("source",14))
txtAñadStk.place(relx=0.15,rely=0.13)

txtMercad = Label(ventAñadir, text="Mercaderia",bg="#EBF5FB", font=("courier",11))
txtMercad.place(relx=0.15,rely=0.25)

txtCant = Label(ventAñadir, text="Cantidad", bg="#EBF5FB", font=("courier",11))
txtCant.place(relx=0.49,rely=0.25)

txtFecha = Label(ventAñadir, text="Fecha", bg="#EBF5FB", font=("courier",11))
txtFecha.place(relx=0.15,rely=0.34)

txtUsr = Label(ventAñadir, text="Usuario", bg="#EBF5FB", font=("courier",11))
txtUsr.place(relx=0.49,rely=0.34)

txtUsuario = Label(ventAñadir, text="Actual",bg="#EBF5FB", font=("courier",11))
txtUsuario.place(relx=0.6,rely=0.34)

txtStockRec = Label(ventAñadir, text="Stocks añadidos",bg="#D5F5E3", font=("Source",13))
txtStockRec.place(relx=0.146,rely=0.52)
#Botones

btnCalc = Button(ventAñadir,command=calcu, text="Calculadora",bg ="#D6EAF8",bd=0,width="9")
btnCalc.place(relx=0.71,rely=0.24)

btnAñadir = Button(ventAñadir, text="Añadir",bg="#D6EAF8",font=("Source",11),bd=0,width="9")
btnAñadir.place(relx=0.786,rely=0.44)

#Entrys
entryCant = Entry(ventAñadir,width="10")
entryCant.place(relx=0.6, rely=0.25)

#Comboboxs
comboMercad = ttk.Combobox(ventAñadir,state="readonly",width="10",values=["Medialunas","pinchadas","raspadas"])
comboMercad.place(relx=0.28,rely=0.25)


comboFecha = ttk.Combobox(ventAñadir,state="readonly",width="10",values=
["Actual(hoy)","Otra"])
comboFecha.place(relx=0.28,rely=0.34)

#_


#   __

#   Frame Inferior
frameInf = Frame(ventAñadir,bg="black",width="800",height="20")
frameInf.place(relx=0,rely=0.966)

#Labels
txtUsr = Label(frameInf,text="Usuario:",fg="white",bg="black", font=("source",10))
txtUsr.place(relx=0.75,rely=0)


#_


#   __
#__

ventAñadir.mainloop()