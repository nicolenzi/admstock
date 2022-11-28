import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3

ventanaPed = tk.Tk()
ventanaPed.title("Pedidos")
ventanaPed.geometry("800x600")
ventanaPed.configure(bg="#AED6F1")

#frames
frameOpc = Frame(ventanaPed,
           width="90",
           height="600",
           bg="#85C1E9")
frameOpc.pack(side=LEFT)

frameCentro = Frame(ventanaPed,
           width="710",
           height="600",
           bg="snow")
frameCentro.pack(side=LEFT)

#Labels
txtFecha = Label(frameCentro,
            text="fecha",
            bg="snow")
txtFecha.grid(row=0,column=0)


ventanaPed.mainloop()