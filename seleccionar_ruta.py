import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename



def seleccionar_ruta():

    root = tk.Tk()
    root.withdraw()
    archivo_path = asksaveasfilename(defaultextension=".xlsx",filetypes=[("Excel","*xlsx"),("All files","*.*")],title="Guardar fichero como")
    return archivo_path