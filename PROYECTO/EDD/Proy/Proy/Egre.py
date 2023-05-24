import csv
import ArbolAVL
class Egresados:
    def __init__(self, archivo):
        self.arbol_nombres = ArbolAVL
        with open('C:/Users/52999/OneDrive/Desktop/ESTRUCTURA DE DATOS V2/PROYECTO/EDD/Proy/Proy/Egresados.csv', 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv, delimiter=',')
            for nombre, profesion, promedio in lector_csv:
                self.arbol_nombres.insertar(nombre)
    
    def buscar_egresado(self, nombre):
        nodo = self.arbol_nombres.buscar(nombre)
        if nodo is None:
            print("No se encontró ningún egresado con ese nombre.")
        else:
            print("Egresado encontrado:")
            print(f"Nombre: {nodo.valor}")
            # Aquí se podrían agregar más atributos del egresado, como su profesión y promedio.


if __name__=='__main__':
    egresados = Egresados(Egresados)
    egresados.buscar_egresado('Abril Guadalupe Escobedo Bojórquez')

