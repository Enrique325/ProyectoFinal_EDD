import csv
from ArbolAVL import ArbolAVL

class Egresados:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.arbol = ArbolAVL()
        #self.datos_alumnos = []

    def cargar_datos(self):
        contador = 0
        with open(self.archivo_csv, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv, delimiter=',')
            next(lector_csv)
            for fila in lector_csv:
                if contador >= 626:
                    break
                nombre = fila[0]
                self.arbol.agregar(nombre)
                #profesion = fila[1]
                #promedio = float(fila[2])
                #self.datos_alumnos.append((nombre, profesion, promedio))
                contador += 1
                #print("--------------------------------------------------------------------------------------------------------------------------------")
                #print(f"Nombre: {nombre}, Profesión: {profesion}, Promedio: {promedio}")
                #print("--------------------------------------------------------------------------------------------------------------------------------")
                
    def imprimir_arbol(self):
        self.arbol.imprimir_arbol()
        
    def buscar_nombre(self, nombre):
        resultado = self.arbol.buscar(nombre)
        if resultado:
            print(f"{nombre} encontrado en el árbol")
        else:
            print(f"{nombre} no encontrado en el árbol")

# Ejemplo de uso
egresados = Egresados('Egresados.csv')
egresados.cargar_datos()
