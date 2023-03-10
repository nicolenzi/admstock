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
    btnBuscar_Buscador = Button(ventBuscar,text="Buscar",command=buscador_datos)
    btnBuscar_Buscador.grid(row=4,column=0)
    
    #TXT
    txtBuscar = Label(ventBuscar,text="Tipo de dato:")
    txtBuscar.grid(row=0,column=0)

    txtOrden = Label(ventBuscar,text="ID / MERCADERIA / CANTIDAD / FECHA / USUARIO")
    txtOrden.grid(row=0,column=2)

    txtBusqueda = Label(ventBuscar,text="Dato a buscar:")
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
    txtID = Label(ventModificar,text="ID ")
    txtID.grid(row=0,column=0)

    txtListado = Label(ventModificar,text="Seleccione una ID para modificar")
    txtListado.grid(row=1,column=0,columnspan=4,padx=3,pady=6)

    txtCambiar = Label(ventModificar,text="Cambiar ")
    txtCambiar.grid(row=2,column=0)

    txtPor = Label(ventModificar,text="por ")
    txtPor.grid(row=2,column=2)

    #Entrys
   

    entryMod = Entry(ventModificar,width="12")
    entryMod.grid(row=2,column=3)

    entryId = Entry(ventModificar,width="4")
    entryId.grid(row=0,column=1)
    
    #Btn
    
    btnConfID = Button(ventModificar,text="Buscar",command=verID)
    btnConfID.grid(row=0,column=2) 
    
    btnConfirm = Button(ventModificar,text="Confirmar",command=modStock)
    btnConfirm.grid(row=2,column=4)


    #Combobox
    comboCambio = ttk.Combobox(ventModificar,values=["Mercaderia","Cantidad","Fecha","Usuario"],width="10")
    comboCambio.grid(row=2,column=1)
    





    ventModificar.mainloop()

def Eliminar():
    ventElimin = Toplevel()
    ventElimin.geometry("300x200")
    ventElimin.title("Eliminar stock")
    
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
    txtID.grid(row=0,column=0)

    #Entry
    entryID = Entry(ventElimin,width="5")
    entryID.grid(row=0,column=1)

    #List
    listID = Listbox(ventElimin,width="30",height="1",bd=0)
    listID.grid(row=1,column=0,columnspan=2)
    
    #Btn
    btnElimBD = Button(ventElimin,text="Eliminar stock",command=ElimBD)
    btnElimBD.grid(row=1,column=3)
    
    btnBuscID = Button(ventElimin,text="Buscar",command=InsID)
    btnBuscID.grid(row=0,column=2) 

    ventElimin.mainloop()

    print("ELIMINAR")


    


#Frames
frameOpc = Frame(ventanaList, bg="#85C1E9", width="100", height="560")
frameOpc.grid(row=0,column=0)

frameCent = Frame(ventanaList, bg="white", width="700", height="560")
frameCent.grid(row=0,column=1)

#btn
btnBuscar = Button(frameCent, bg="white", text="Buscar",command=Buscador,bg="#EBF5FB")
btnBuscar.place(relx=0.7,rely=0.4)

btnMod = Button(frameCent,bg="white", text="Modificar",command=Modificador,bg="#EBF5FB")
btnMod.place(relx=0.7,rely=0.5)

btnElim = Button(frameCent,bg="white",text="Eliminar",command=Eliminar,bg="#EBF5FB")
btnElim.place(relx=0.7,rely=0.6)



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

btnAct = Button(ventanaList,bg="White",text="Actualizar",command=Actualizar)
btnAct.place(relx=0.739,rely=0.65)




frameUsuario = Frame(ventanaList, bg="black", width="800", height="40")
frameUsuario.grid(row=2,column=0,columnspan=2)

frameGridList = Frame(frameCent, bg="orange", width="550", height="380")
frameGridList.place(relx=0.1,rely=0.27) 

#Labels

txtListP = Label(frameCent, text="Listado de pedidos", font=("Arial",14),bg="#EBF5FB")
txtListP.place(relx=0.1,rely=0.2)

txtNum = Label(frameGridList, text="ID", font=("Calabri",12),bg="#EBF5FB")
txtNum.grid(row=0,column=0,ipadx=10)

txtMercad = Label(frameGridList, text="Producto",font=("Calabri",12),bg="#EBF5FB")
txtMercad.grid(row=0,column=1,ipadx=10)

txtCant = Label(frameGridList, text="Cantidad",font=("Calabri",12),bg="#EBF5FB")
txtCant.grid(row=0,column=2, ipadx=10)

txtFecha = Label(frameGridList, text="Fecha",font=("Calabri",12),bg="#EBF5FB")
txtFecha.grid(row=0,column=3, ipadx=12)

txtUsr = Label(frameGridList, text="Usuario",font=("Calabri",12),bg="#EBF5FB")
txtUsr.grid(row=0,column=4, ipadx=16)

ventanaList.mainloop()
sqlconex.close()