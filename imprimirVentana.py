import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.filedialog import asksaveasfilename



def imprimirVentana(opcion_seleccionada):

    root = tk.Tk()
    root.withdraw()

    while True:
        if opcion_seleccionada=='1':
            messagebox.showinfo("Seleccione fichero", "Seleccione fichero con las certificaciones")
            root.destroy()
            break
        elif opcion_seleccionada=='2':
            messagebox.showinfo("Seleccione fichero", "Seleccione fichero con las NCs, textos de NC's y comentarios")
            root.destroy()
            break
        elif opcion_seleccionada=='3':
            messagebox.showinfo("Seleccione fichero", "Seleccione fichero con las NCs, textos de NC's y comentarios")
            root.destroy()
            break
        elif opcion_seleccionada=='4':
            messagebox.showinfo("Seleccione fichero", "Seleccione fichero con las NCs, textos de NC's y comentarios")
            root.destroy()
            break
        elif opcion_seleccionada=='5':
            messagebox.showinfo("Seleccione fichero", "Seleccione fichero con las NCs, textos de NC's y comentarios")
            root.destroy()
            break
        elif opcion_seleccionada == '6':
            messagebox.showinfo("Seleccione fichero", "Seleccione fichero con las horas de REP")
            root.destroy()
        elif opcion_seleccionada == '8':
            messagebox.showinfo("Seleccione fichero", "Seleccione fichero con las horas de cierre de mes, las horas del mes en curso y la hoja de certificaciones, en este sentido")
            root.destroy()
            break
