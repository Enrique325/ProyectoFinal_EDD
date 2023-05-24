import pandas as pd
import tkinter as tk
from openpyxl import load_workbook
import arbolPromedio as arbolPromedio
import arbolNombres as arbolNombres
import arbolProfesion as arbolProfesion

# Resto de tu código...

def mostrar_datos(indices):
    resultado_text.delete(1.0, tk.END)
    for indice in indices:
        if isinstance(indice, int) and indice <= len(df):
            fila = df.iloc[indice-1]
            resultado_text.insert(tk.END, f"Nombre del Alumno: {fila['Nombre del Alumno']}\n")
            resultado_text.insert(tk.END, f"Profesión: {fila['Profesión']}\n")
            resultado_text.insert(tk.END, f"Promedio: {fila['Promedio']}\n")
            resultado_text.insert(tk.END, "-----------------\n")

def obtener_datos():
    profesion = profesion_entry.get()
    promedio = promedio_entry.get()

    if profesion and promedio:
        egresados_combinacion = arbolPromedios.buscar_por_combinacion(profesion, float(promedio))
        mostrar_datos(egresados_combinacion)
    elif profesion:
        egresados_profesion = arbolProfesion.buscar_por_profesion(profesion)
        mostrar_datos(egresados_profesion)
    elif promedio:
        egresados_promedio = arbolPromedios.buscar_por_calificacion(float(promedio))
        mostrar_datos(egresados_promedio)
    else:
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, "No se especificaron criterios de búsqueda.")

root = tk.Tk()
root.title("Búsqueda de Egresados")
root.geometry("500x500")

profesion_label = tk.Label(root, text="Profesión:")
profesion_label.pack()

profesion_entry = tk.Entry(root)
profesion_entry.pack()

promedio_label = tk.Label(root, text="Promedio:")
promedio_label.pack()

promedio_entry = tk.Entry(root)
promedio_entry.pack()

resultado_text = tk.Text(root, height=20)
resultado_text.pack()

buscar_button = tk.Button(root, text="Buscar", command=obtener_datos)
buscar_button.pack()

# Crear los árboles y cargar los datos

if __name__ == '__main__':
    arbolPromedios = arbolPromedio.ArbolAVL()
    arbolesNombres = arbolNombres.ArbolAVL()
    arbolProfesion = arbolProfesion.ArbolAVL()
    
    # Resto de tu código...
    
    root.mainloop()

workbook.close()
