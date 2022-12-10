import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

ventanaList = tk.Tk()
ventanaList.title("Lista de stocks")
ventanaList.geometry("800x600")
ventanaList.configure(bg="white")

#Frames
frameOpc = Frame(ventanaList, bg="#85C1E9", width="100", height="560")
frameOpc.grid(row=0,column=0)
frameCent = Frame(ventanaList, bg="snow", width="700", height="560")
frameCent.grid(row=0,column=1)
frameUsuario = Frame(ventanaList, bg="black", width="800", height="40")
frameUsuario.grid(row=2,column=0,columnspan=2)

frameGridList = Frame(frameCent, bg="orange", width="550", height="380")
frameGridList.place(relx=0.1,rely=0.27) 

#Labels

txtListP = Label(frameCent, text="Listado de pedidos", font=("Arial",14))
txtListP.place(relx=0.1,rely=0.2)

txtNum = Label(frameGridList, text="Nro", font=("Calabri",12))
txtNum.grid(row=0,column=0,ipadx=10)

txtMercad = Label(frameGridList, text="Producto",font=("Calabri",12))
txtMercad.grid(row=0,column=1,ipadx=20)

txtCant = Label(frameGridList, text="Cantidad",font=("Calabri",12))
txtCant.grid(row=0,column=2, ipadx=20)

txtFecha = Label(frameGridList, text="Fecha",font=("Calabri",12))
txtFecha.grid(row=0,column=3, ipadx=20)

txtUsr = Label(frameGridList, text="Usuario",font=("Calabri",12))
txtUsr.grid(row=0,column=4, ipadx=20)

ventanaList.mainloop()
