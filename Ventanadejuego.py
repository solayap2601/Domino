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
        self.geometry("300x275")
        self.title("Dominó UNAL")
        self.option_add("*tearOff", False)
        self.resizable(False,False)
        self.iconbitmap('icono.ico')
