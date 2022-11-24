import tkinter as tk
from tkinter import *
from tkinter import messagebox


ventanaP = tk.Tk()
ventanaP.title("Ventana principal")
ventanaP.geometry("800x600")
ventanaP.configure(bg = "#AED6F1")

#Frames
frameUrsInfo = Frame(ventanaP,
                    width="800",
                    height="30",
                    bg="black")
frameUrsInfo.pack(side=BOTTOM)

frameOpc = Frame(ventanaP,
                    width="50",
                    height="570",
                    bg="#85C1E9")
frameOpc.pack(side=LEFT)

frameCentro = Frame(ventanaP,
              width="750",
              height="570",
              bg="snow")
frameCentro.pack(side=LEFT)



ventanaP.mainloop()