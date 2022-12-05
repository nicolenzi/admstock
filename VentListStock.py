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

ventanaList.mainloop()
