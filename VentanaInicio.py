from Ventanadejuego import VentanaSecundaria
from tkinter import messagebox as MessageBox, ttk 
from tkinter import *
import tkinter as tk
import os
import pathlib
path = os.path.join(pathlib.Path(__file__).parent.absolute())

class ventanaInicio(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        # Editamos nuestra ventana
        self.geometry("300x275")
        self.title("Dominó UNAL")
        self.option_add("*tearOff", False)
        self.resizable(False,False)
        self.iconbitmap('icono.ico')
        self.frame1 = tk.Frame(self, width=300, height=400, borderwidth=15, bg="Green")
        self.frame1.pack()
        self.etiquetaBienvenida = Label(self.frame1, text="¡Hola!\n Bienvenido al dominó \n UNAL", font=("Segoe UI", 20), bg="Green")
        self.etiquetaBienvenida.pack(expand = True)
        self.autores = Label(self.frame1, text="Por:\n Sebastián Olaya Pérez\n Juan Diego Ortiz Tabares\n Juan Camilo Torres Arboleda\n Juan José Marin Alvarez", font=("Segoe UI", 8), bg="Green")
        self.autores.pack(pady = 10)
        self.botonJugar = Button(self.frame1, text = "JUGAR", font=("Segoe UI", 13), command = self.abrirVentanaSecundaria)
        self.botonJugar.pack()

    def abrirVentanaSecundaria(self):
         #if not VentanaSecundaria.en_uso:
            self.ventanaUsuario = VentanaSecundaria()
            self.ventanaUsuario.ventanaInicio = self
            self.iconify()

if __name__ == "__main__":
    ventana_inicios = ventanaInicio()
    ventana_inicios.mainloop()
