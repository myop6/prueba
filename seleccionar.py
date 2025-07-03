import tkinter as tk
from tkinter import filedialog


def seleccionar():

    root=tk.Tk()
    root.withdraw()
    archivo_path=filedialog.askopenfilename(title="Seleccione archivo Excel", filetypes=[("Excel files", "*.xlsx *.xls")])
    return archivo_path