import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

ventanaList = tk.Tk()
ventanaList.title("Lista de stocks")
ventanaList.geometry("800x600")
ventanaList.configure(bg="white")

#SQL conexion
sqlconex = sql.connect("StockBD.db")
curs = sqlconex.cursor()


def Buscador():

    ventBuscar = Toplevel()
    ventBuscar.geometry("380x200")
    ventBuscar.title("Buscador")
    ventBuscar.configure(bg="white")
    
    def buscador_datos():
        valcombo = comboBus.get()
        valentry = entryValBusc.get()

        if valcombo == "Mercaderia":
            curs.execute('''SELECT * FROM stock WHERE Mercaderia = ?''',(valentry,))
            sqlconex.commit()
            rsMerc = curs.fetchall()
            
            indice = 0
            for listado in rsMerc:
                listResBusc.insert(indice,rsMerc[indice])
                indice= indice + 1            

        elif valcombo == "Cantidad":
            curs.execute('''SELECT * FROM stock WHERE Cantidad = ?''',(valentry,))
            sqlconex.commit()
            rsPro = curs.fetchall()

            indice = 0
            for listado in rsPro:
                listResBusc.insert(indice,rsPro[indice])
                indice = indice + 1

        elif valcombo == "Fecha":
            curs.execute('''SELECT * FROM stock WHERE Fecha = ?''',(valentry,))
            sqlconex.commit()
            rsFech = curs.fetchall()

            indice = 0
            for listado in rsFech:
                listResBusc.insert(indice,rsFech[indice])
                indice = indice + 1
        
        elif valcombo == "Usuario":
            curs.execute('''SELECT * FROM stock WHERE Usuario = ?''',(valentry,))
            sqlconex.commit()
            rsUsr = curs.fetchall()

            indice = 0
            for listado in rsUsr:
                listResBusc.insert(indice,rsUsr[indice])
                indice = indice + 1

        else:
            print("Valor invalido")



    #Combo
    comboBus = ttk.Combobox(ventBuscar,state="readonly",values=["Mercaderia","Cantidad","Fecha","Usuario"],width="10")
    comboBus.grid(row=1,column=0)

    #Btn
    btnBuscar_Buscador = Button(ventBuscar,text="Buscar",command=buscador_datos,bd=0)
    btnBuscar_Buscador.grid(row=4,column=0)
    
    #TXT
    txtBuscar = Label(ventBuscar,text="Tipo de dato:",bg="#EBF5FB")
    txtBuscar.grid(row=0,column=0)

    txtOrden = Label(ventBuscar,text="ID / MERCADERIA / CANTIDAD / FECHA / USUARIO",bg="#EBF5FB")
    txtOrden.grid(row=0,column=2)

    txtBusqueda = Label(ventBuscar,text="Dato a buscar:",bg="#EBF5FB")
    txtBusqueda.grid(row=2,column=0)

    #Entrys
    entryValBusc = Entry(ventBuscar,width="13")
    entryValBusc.grid(row=3,column=0,padx=5)

    #Listbox

    listResBusc = Listbox(ventBuscar,width="40",height="10")
    listResBusc.grid(row=1,column=2,rowspan=4)

def Modificador():
    ventModificar = Toplevel()
    ventModificar.geometry("320x100")
    ventModificar.title("Modificador")
    ventModificar.configure(bg="white")
    
    def verID():
        
        valorID = str(entryId.get())
        curs.execute('''SELECT * FROM stock WHERE ID = ?''',valorID)
        sqlconex.commit()
        entryID = curs.fetchall()

        txtListado.configure(text=entryID)

    def modStock():
        valorMID = entryId.get()
        valorCombo = comboCambio.get()
        valorMod = entryMod.get()
        print(valorMID,valorCombo,valorMod)

        if valorCombo == "Mercaderia":

            curs.execute('''UPDATE stock SET Mercaderia = ? WHERE id = ?''',(valorMod,valorMID,))
            sqlconex.commit()
            ModificacionM  = curs.fetchall()
            print(ModificacionM)
        
        elif valorCombo == "Cantidad":
            curs.execute('''UPDATE stock SET Cantidad = ? WHERE id = ?''',(valorMod,valorMID,))
            sqlconex.commit()
            ModificacionC = curs.fetchall()
            print(ModificacionC)

            
        elif valorCombo == "Fecha":
            curs.execute('''UPDATE stock SET Fecha = ? WHERE id = ?''',(valorMod,valorMID,))
            sqlconex.commit()
            ModificacionF = curs.fetchall()
            print(ModificacionF)

        elif valorCombo == "Usuario":
            curs.execute('''UPDATE stock SET Usuario = ? WHERE id = ?''',(valorMod,valorMID,))
            sqlconex.commit()
            ModificacionU = curs.fetchall()
            print(ModificacionU)

        else:
            print("ERROR")


    #TXT
    txtID = Label(ventModificar,text="ID ",bg="#EBF5FB")
    txtID.grid(row=0,column=0,padx=0,sticky=E)

    txtListado = Label(ventModificar,text="Seleccione una ID para modificar",bg="#EBF5FB")
    txtListado.grid(row=1,column=0,columnspan=4,padx=3,pady=15)

    txtCambiar = Label(ventModificar,text="Cambiar ",bg="#EBF5FB")
    txtCambiar.grid(row=2,column=0)

    txtPor = Label(ventModificar,text="por ",bg="#EBF5FB")
    txtPor.grid(row=2,column=2)

    #Entrys
   

    entryMod = Entry(ventModificar,width="12")
    entryMod.grid(row=2,column=3)

    entryId = Entry(ventModificar,width="4")
    entryId.grid(row=0,column=1,sticky=W)
    
    #Btn
    
    btnConfID = Button(ventModificar,text="Buscar",command=verID,bd=0)
    btnConfID.grid(row=0,column=2) 
    
    btnConfirm = Button(ventModificar,text="Confirmar",command=modStock,bd=0,bg="#ABEBC6")
    btnConfirm.grid(row=2,column=4)


    #Combobox
    comboCambio = ttk.Combobox(ventModificar,values=["Mercaderia","Cantidad","Fecha","Usuario"],width="8")
    comboCambio.grid(row=2,column=1)
    





    ventModificar.mainloop()

def Eliminar():
    ventElimin = Toplevel()
    ventElimin.geometry("300x80")
    ventElimin.title("Eliminar stock")
    ventElimin.configure(bg="white")
    
    def ElimBD():

        valorID = entryID.get()
        curs.execute('''DELETE FROM stock WHERE id = ?''',valorID)
        sqlconex.commit()

        print("eliminado")
    
    def InsID():
        getID = entryID.get()
        curs.execute('''SELECT * FROM stock WHERE id = ?''',getID)
        sqlconex.commit()
        datosElim = curs.fetchall()

        listID.insert(0,datosElim)

        print(datosElim)
    #txt
    txtID = Label(ventElimin,text="ID: ")
    txtID.grid(row=0,column=0,sticky=E)

    #Entry
    entryID = Entry(ventElimin,width="5")
    entryID.grid(row=0,column=1,sticky=W)

    #List
    listID = Listbox(ventElimin,width="30",height="1",bd=0)
    listID.grid(row=1,column=0,columnspan=3,padx=5)
    
    #Btn
    btnElimBD = Button(ventElimin,text="Eliminar stock",command=ElimBD,bg="#EC7063",fg="white")
    btnElimBD.grid(row=1,column=3,pady=15)
    
    btnBuscID = Button(ventElimin,text="Buscar",command=InsID)
    btnBuscID.grid(row=0,column=2) 

    ventElimin.mainloop()

    print("ELIMINAR")


    


#Frames
frameOpc = Frame(ventanaList, bg="#EBF5FB", width="115", height="570")
frameOpc.grid(row=0,column=0)

frameCent = Frame(ventanaList, bg="white", width="700", height="570")
frameCent.grid(row=0,column=1)

frameAbajo = Frame(ventanaList, bg="black", width="815", height="30")
frameAbajo.grid(row=2,column=0,columnspan=2)

frameGridList = Frame(frameCent, bg="orange", width="550", height="380")
frameGridList.place(relx=0.1,rely=0.27)

#btn
btnBuscar = Button(frameCent, bg="#58D68D",fg="white",text="Buscar",command=Buscador,bd=0,font=("courier",10))
btnBuscar.place(relx=0.7,rely=0.4)

btnMod = Button(frameCent,bg="#F7DC6F",fg="white", text="Modificar",command=Modificador,bd=0,font=("courier",10))
btnMod.place(relx=0.7,rely=0.5)

btnElim = Button(frameCent,bg="#EC7063",fg="white",text="Eliminar",command=Eliminar,bd=0,font=("courier",10))
btnElim.place(relx=0.7,rely=0.6)

btnVolver = Button(frameOpc,text="Volver",font=("courier",10),bg="red",fg="white",bd=0,width="14")
btnVolver.place(relx=0,rely=0.96)



#Listboxs 

listbNro = Listbox(frameCent, bg="white",width="5",height="18", bd=0)
listbNro.place(relx=0.1,rely=0.32)

listbProduc = Listbox(frameCent, bg="white", width="12",height="18", bd=0)
listbProduc.place(relx=0.17,rely=0.32)

listbCant = Listbox(frameCent, bg="white",width="12", height="18", bd=0)
listbCant.place(relx=0.3,rely=0.32)

listbFech = Listbox(frameCent, bg="white", width="10", height="18", bd=0)
listbFech.place(relx=0.43,rely=0.32)

listbUsr = Listbox(frameCent, bg="white", width="12", height="18", bd=0)
listbUsr.place(relx=0.54,rely=0.32)


curs.execute('''SELECT id FROM stock''')
BDlistNro = curs.fetchall()
curs.execute('''SELECT Mercaderia FROM stock''')
BDlistProd = curs.fetchall()
curs.execute('''SELECT Cantidad FROM stock''')
BDlistCant = curs.fetchall()
curs.execute('''SELECT Fecha FROM stock''')
BDlistFech = curs.fetchall()
curs.execute('''SELECT Usuario FROM stock''')
BDlistUsr = curs.fetchall()


index = 0
for lista in BDlistNro:
    listbNro.insert(index,BDlistNro[index])
    listbProduc.insert(index,BDlistProd[index])
    listbCant.insert(index,BDlistCant[index])
    listbFech.insert(index,BDlistFech[index])
    listbUsr.insert(index,BDlistUsr[index])
    index = index + 1

def Actualizar():
    valorzise = listbNro.size()
    listbNro.delete(0,valorzise)    
   
    index = 0
    


    for listas in BDlistNro:

        listbNro.insert(index,BDlistNro[index])

        listbProduc.insert(index,BDlistProd[index])
        listbCant.insert(index,BDlistCant[index])
        listbFech.insert(index,BDlistFech[index])
        listbUsr.insert(index,BDlistUsr[index])
        index = index + 1

        

    print(valorzise)

#btnAct = Button(ventanaList,bg="White",text="Actualizar",command=Actualizar)
#btnAct.place(relx=0.739,rely=0.65)
 

#Labels

imgFrzn = PhotoImage(file="imagenes/titulo.png")
imgLogo = Label(frameOpc, image=imgFrzn,width="110",height="45")
imgLogo.place(relx=0,rely=0)

txtListP = Label(frameCent, text="Listado de pedidos", font=("courier",14),bg="#EBF5FB")
txtListP.place(relx=0.1,rely=0.2)

txtNum = Label(frameGridList, text="ID", font=("courier",10),bg="#EBF5FB")
txtNum.grid(row=0,column=0,ipadx=10)

txtMercad = Label(frameGridList, text="Producto",font=("courier",10),bg="#EBF5FB")
txtMercad.grid(row=0,column=1,ipadx=10)

txtCant = Label(frameGridList, text="Cantidad",font=("courier",10),bg="#EBF5FB")
txtCant.grid(row=0,column=2, ipadx=10)

txtFecha = Label(frameGridList, text="Fecha",font=("courier",10),bg="#EBF5FB")
txtFecha.grid(row=0,column=3, ipadx=12)

txtUsr = Label(frameGridList, text="Usuario",font=("courier",10),bg="#EBF5FB")
txtUsr.grid(row=0,column=4, ipadx=16)

#_FA
txtUsrAbj = Label(frameAbajo,text="Usuario: ",font=("courier",10),bg="black",fg="white")
txtUsrAbj.place(relx=0.75,rely=0.1)



ventanaList.mainloop()
sqlconex.close()