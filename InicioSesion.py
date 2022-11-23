import tkinter as tk
from tkinter import * 
from tkinter import messagebox

#colores
#Celeste1: #5DADE2 
#Celeste2: #85C1E9
#Celeste3: #AED6F1

ventanaI = tk.Tk()
ventanaI.title("Inicio de sesion")
ventanaI.geometry("600x400")
ventanaI.configure(bg ="#85C1E9")

#Labels
textoFrozen = Label(ventanaI,
                text="Frozen",
                font=("Calabri",30),
                bg="#85C1E9")
textoFrozen.place(relx=0.17,rely=0.35)

textoSesion = Label(ventanaI,
                text="Inicio de sesion",
                font=("Arial",15),
                bg="#85C1E9")
textoSesion.place(relx=0.16, rely=0.5)

textoUsuario = Label(ventanaI,
                text="Usuario:",
                font=("Arial",10),
                bg="#85C1E9")
textoUsuario.place(relx=0.5,rely=0.4)

textoContraseña = Label(ventanaI,
                text="Contraseña",
                font=("Arial",10),
                bg="#85C1E9")
textoContraseña.place(relx=0.5,rely=0.5)


#Entrys
entryUsr = Entry(ventanaI)
entryUsr.place(relx=0.65,rely=0.39)

entryContr = Entry(ventanaI)
entryContr.place(relx=0.65,rely=0.48)


ventanaI.mainloop()