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
sqlconex = sql.connect("StockBD.db")
curs = sqlconex.cursor()

# curs.execute('''INSERT INTO Mercaderia ("Tortas raspadas")VALUES (0)''')
# curs.execute('''INSERT INTO Mercaderia ("Medialunas")VALUES (0)''')

#           METODOS

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

def Añadir():
    CM = str(comboMercad.get())
    EC = int(entryCant.get())
    EF = str(date.today())
    EU = str(entryUsr.get())


    

    #curs.execute('''INSERT INTO stock ("Mercaderia","Cantidad","Fecha") VALUES (?,?,?)''',(CM,EC,EF))
    #sqlconex.commit()
    
    listStockM1.insert(0,str(CM))
    listStockC2.insert(0,EC)
    listStockF3.insert(0,EF)
    listStockU4.insert(0,EU)

def A():
    
   confM = str(listStockM1.get(0))
   confC = listStockC2.get(0)
   confF = listStockF3.get(0)
   confU = listStockU4.get(0)

   curs.execute('INSERT INTO stock ("Mercaderia","Cantidad","Fecha","Usuario") VALUES (?,?,?,?)',(confM,confC,confF,confU))
   sqlconex.commit()

   print(confM,confC,confC,confU)
    
#__

#           FRAMES
#   Frame Izquierdo
frameIzq = Frame(ventAñadir, bg="#EBF5FB",width="125",height="580")
frameIzq.place(relx=0,rely=0)

#Labels
imgFrzn = PhotoImage(file="imagenes/titulo.png")
txtFrozen = Label(ventAñadir,image=imgFrzn,width="110",height="50")
txtFrozen.grid(row=0,column=0,padx=10)
#_

#Botones
btnVolver = Button(ventAñadir, text="Volver",fg="white",bg="red", bd=0, width="17",)
btnVolver.place(relx=0,rely=0.93)
#_


#   __

#   Frame centro
frameCent = Frame(ventAñadir, bg="white", width="690",height="580")
frameCent.place(relx=0.155,rely=0)

frameBg1 = Frame(frameCent, bg="#EBF5FB",width="600",height="150")
frameBg1.place(relx=0.05,rely=0.2)

frameBg2 = Frame(frameCent, bg="#D5F5E3",width="600",height="60")
frameBg2.place(relx=0.05,rely=0.57)

#Labels
txtAñadStk = Label(ventAñadir, text="Añadir stock",bg="#EBF5FB", font=("source",14))
txtAñadStk.place(relx=0.20,rely=0.13)

txtMercad = Label(ventAñadir, text="Mercaderia",bg="#EBF5FB", font=("courier",11))
txtMercad.place(relx=0.25,rely=0.25)

txtCant = Label(ventAñadir, text="Cantidad", bg="#EBF5FB", font=("courier",11))
txtCant.place(relx=0.54,rely=0.25)

txtFecha = Label(ventAñadir, text="Fecha", bg="#EBF5FB", font=("courier",11))
txtFecha.place(relx=0.25,rely=0.34)

txtFechaA = Label(ventAñadir, text=date.today(),bg="#EBF5FB",font=("courier",9))
txtFechaA.place(relx=0.33,rely=0.34)

txtUsr = Label(ventAñadir, text="Usuario", bg="#EBF5FB", font=("courier",11))
txtUsr.place(relx=0.54,rely=0.34)

txtUsuario = Label(ventAñadir, text="(USR)",bg="#EBF5FB", font=("courier",11))
txtUsuario.place(relx=0.76,rely=0.34)

#

txtStockAñad = Label(ventAñadir, text="Stock añadido",bg="#D5F5E3", font=("Source",14))
txtStockAñad.place(relx=0.20,rely=0.49)


txtListMerc = Label(ventAñadir,text="Mercaderia",bg="#D5F5E3",font=("courier",11))
txtListMerc.place(relx=0.3,rely=0.56)

txtListCant = Label(ventAñadir,text="Cantidad",bg="#D5F5E3",font=("courier",11))
txtListCant.place(relx=0.47,rely=0.56)

txtListFecha = Label(ventAñadir,text="Fecha",bg="#D5F5E3",font=("courier",11))
txtListFecha.place(relx=0.6,rely=0.56)

txtListUsr = Label(ventAñadir,text="Usuario",bg="#D5F5E3",font=("courier",11))
txtListUsr.place(relx=0.74,rely=0.56)



#Botones

btnCalc = Button(ventAñadir,command=calcu, text="Calculadora",bg ="#D6EAF8",bd=0,width="9")
btnCalc.place(relx=0.75,rely=0.24)

btnAñadir = Button(ventAñadir, text="Añadir",bg="#D6EAF8",font=("Source",11),bd=0,width="9",command=Añadir)
btnAñadir.place(relx=0.84,rely=0.44)

#

btnConfirm = Button(ventAñadir,command=A, text="Confirmar",bg="#ABEBC6",bd=0,width="9",font=("Source",11))
btnConfirm.place(relx=0.84,rely=0.65)

#Entrys
entryCant = Entry(ventAñadir,width="10")
entryCant.place(relx=0.65, rely=0.25)

entryUsr = Entry(ventAñadir,width="12")
entryUsr.place(relx=0.65,rely=0.34)
#Comboboxs
comboMercad = ttk.Combobox(ventAñadir,state="readonly",width="10",values=["Medialunas","pinchadas","raspadas"])
comboMercad.place(relx=0.38,rely=0.25)

#Listboxs
listStockM1 = Listbox(ventAñadir,bg="#D5F5E3",bd=1,width="25",height="1")
listStockM1.place(relx=0.27,rely=0.6)

listStockC2 = Listbox(ventAñadir,bg="#D5F5E3",bd=1, width="13",height="1")
listStockC2.place(relx=0.47,rely=0.6)

listStockF3 = Listbox(ventAñadir,bg="#D5F5E3",bd=1, width="15",height="1")
listStockF3.place(relx=0.58,rely=0.6)

listStockU4 = Listbox(ventAñadir,bg="#D5F5E3",bd=1,width="20",height="1")
listStockU4.place(relx=0.706,rely=0.6)
#_


#   __

#   Frame Inferior
frameInf = Frame(ventAñadir,bg="black",width="800",height="30")
frameInf.place(relx=0,rely=0.966)

#Labels
txtUsr = Label(frameInf,font=("courier",9),
         text="Usuario: ",fg="white",bg="black")
txtUsr.place(relx=0.75,rely=0)


#_


#   __
#__

ventAñadir.mainloop()

sqlconex.close()
