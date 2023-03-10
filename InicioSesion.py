import time
import tkinter as tk
from tkinter import * 
from tkinter import messagebox
import sqlite3 as sql
import os


usrs = ['nico','lenzi','molina']
conts = ['123','321','abc']

ventanaI = tk.Tk()
ventanaI.title("Inicio de sesion")
ventanaI.geometry("600x400")
ventanaI.configure(bg ="#85C1E9")

sqlconex = sql.connect("UsuariosBD.db")
curs = sqlconex.cursor()

def inciarSesion():

    

    usuario = entryUsr.get()
    contra = entryContr.get()
    
   # curs.execute('''SELECT Nombre FROM Usuarios WHERE Nombre = ?''',(usuario,))
   # sqlconex.commit()
   # consultUSR = curs.fetchall()
   # print(consultUSR)
   # if consultUSR == "nico" :
   #     print("ok")
   # elif consultUSR == 'nico':
   #     print("ok2")
   # else:
   #     print("no")

   # curs.execute('''SELECT Contraseña FROM Usuarios WHERE Contraseña = ?''',(contra,))
   # sqlconex.commit()
   # consultContra = curs.fetchall()
    
    if usuario == 'nico' and contra == '1234':
        print("correcto")
        ventanaI.destroy()
        print("ABRIENDO OTRA VENTANA")
        
        
        
        
    else: 
        print("denegado")
    exec(open("VentanaPrincipal.py").read())
    

   
#frame

frmDiv = Frame(ventanaI, width=5,height=180, bg="#AED6F1")
frmDiv.place(relx=0.47,rely=0.3)

#Labels
textoFrozen = Label(ventanaI,
                text="Frozen",
                fg="white",   
                font=("Jomolhari",36),
                bg="#85C1E9")
textoFrozen.place(relx=0.10,rely=0.35)

textoPanif = Label(ventanaI,
                text="Panificados congelados.",
                fg="white",
                font=("Padauk",18),
                bg="#85C1E9")
textoPanif.place(relx=0.06, rely=0.5)

textoUsuario = Label(ventanaI,
                text="Usuario:",
                fg="White",
                font=("Source",12),
                bg="#85C1E9")
textoUsuario.place(relx=0.5,rely=0.39)

textoContraseña = Label(ventanaI,
                text="Contraseña:",
                fg="White",
                font=("Source",12),
                bg="#85C1E9")
textoContraseña.place(relx=0.5,rely=0.5)

txtAvisos = Label(ventanaI, text="Bienvenido!", bg="#ABEBC6", fg="#7DCEA0",width=20)
txtAvisos.place(relx=0.78, rely=0.95)



#Entrys
entryUsr = Entry(ventanaI,bg="#5DADE2",bd="0")
entryUsr.place(relx=0.68,rely=0.39)


entryContr = Entry(ventanaI,bg="#5DADE2",show="*",bd="0")
entryContr.place(relx=0.68,rely=0.5)


#Buttos
botonEntar = Button(ventanaI,
                text="Entrar",
                bd=0,
                width="5",
                fg="white",
                bg="#AED6F1",
                command=inciarSesion)
botonEntar.place(relx=0.74,rely=0.62)



ventanaI.mainloop()
sqlconex.close()