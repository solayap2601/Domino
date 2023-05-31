from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import *
import tkinter as tk
from tkinter import messagebox as MessageBox, ttk 
import sys
import os
import pathlib
path = os.path.join(pathlib.Path(__file__).parent.absolute())

class VentanaSecundaria(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # Editamos nuestra ventana
        self.geometry("1000x600")
        self.title("Dominó UNAL")
        self.option_add("*tearOff", False)
        self.resizable(False,False)
        self.iconbitmap('icono.ico')
# --------------------------------Frame para le puntaje  ---------------------------------------------------------------
        self.frame1 = tk.Frame(self, width=200, height=600,borderwidth=15, bg="brown")
        self.frame1.pack(side="left")
        self.frame1.config(relief="sunken")
        
        self.titulo = Label(self.frame1, text = "PUNTAJE", font = ("Segoe UI", 20))
        self.titulo.place(x = 85, y = 30, anchor ="center")
        
        self.nombre1 = Label(self.frame1, text = "Jugador 1:", font = ("Segoe UI", 15))
        self.nombre1.place(x = 85, y = 85, anchor ="center")
        self.var1 = tk.StringVar()
        self.var1.set("HOLA")
        self.puntaje1 = Label(self.frame1, textvariable = self.var1, font = ("Segoe UI", 15))
        self.puntaje1.place(x = 85, y = 120, anchor ="center")


        self.nombre2 = Label(self.frame1, text = "Jugador 2:", font = ("Segoe UI", 15))
        self.nombre2.place(x = 85, y = 200, anchor ="center")
        self.var2 = tk.StringVar()
        self.var2.set("0")
        self.puntaje1 = Label(self.frame1, textvariable = self.var2, font = ("Segoe UI", 15))
        self.puntaje1.place(x = 85, y = 235, anchor ="center")

        self.nombre3 = Label(self.frame1, text = "Jugador 3:", font = ("Segoe UI", 15))
        self.nombre3.place(x = 85, y = 315, anchor ="center")
        self.var3 = tk.StringVar()
        self.var3.set("0")
        self.puntaje1 = Label(self.frame1, textvariable = self.var3, font = ("Segoe UI", 15))
        self.puntaje1.place(x = 85, y = 350, anchor ="center")

        self.nombre4 = Label(self.frame1, text = "Jugador 4:", font = ("Segoe UI", 15))
        self.nombre4.place(x = 85, y = 430, anchor ="center")
        self.var4 = tk.StringVar()
        self.var4.set("0")
        self.puntaje4 = Label(self.frame1, textvariable = self.var4, font = ("Segoe UI", 15))
        self.puntaje4.place(x = 85, y = 465, anchor ="center")

# ------------------------ Frame para la cantidad de fichas------------------------------------------------------------------
        self.frame2 = tk.Frame(self, width = 800, height = 200,borderwidth = 15, bg ="green")
        self.frame2.pack(side = "top")
        self.frame2.config(relief="sunken")

        self.player1 = Label(self.frame1, text = "Jugador 1:", font = ("Segoe UI", 15))
        self.nombre1.place(x = 85, y = 85, anchor ="center")
        self.var1 = tk.StringVar()
        self.var1.set("HOLA")
        self.puntaje1 = Label(self.frame1, textvariable = self.var1, font = ("Segoe UI", 15))
        self.puntaje1.place(x = 85, y = 120, anchor ="center")