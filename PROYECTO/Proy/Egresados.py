import csv
from ArbolAVLNombre import ArbolAVLNombre
from ArbolAVLProfesion import ArbolAVLProfesion
from ArbolAVLPromedio import ArbolAVLPromedio

class Egresados:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.arbolnombre = ArbolAVLNombre()
        self.arbolprofesion = ArbolAVLProfesion()
        self.arbolpromedio = ArbolAVLPromedio()
        self.datos_alumnos = []

    def cargar_datos(self):
        with open(self.archivo_csv, 'r', encoding='utf-8') as archivo_csv:
            lector_csv = csv.reader(archivo_csv, delimiter=',')
            next(lector_csv)
            for fila in lector_csv:
                nombre = fila[0]
                profesion = fila[1]
                promedio = fila[2]
                self.arbolnombre.insertar(nombre)
                self.arbolprofesion.insertar(profesion)
                self.arbolpromedio.insertar(promedio)
                self.datos_alumnos.append((nombre, profesion, promedio))
        
    def buscar_nombre(self, nombre):
        encontrado = self.arbolnombre.buscar(nombre)
        if encontrado:
            datos_encontrados = [fila for fila in self.datos_alumnos if fila[0] == nombre]
            for nombre, profesion, promedio in datos_encontrados:
                print(f"{nombre} -- {profesion} -- {promedio}.")
        else:
            print(f"No se encontraron egresados con el nombre {nombre}.")
        return encontrado
    
    def buscar_profesion(self, profesion):
        encontrado = self.arbolprofesion.buscar(profesion)
        if encontrado:
            datos_encontrados = [fila for fila in self.datos_alumnos if fila[1] == profesion]
            for nombre, profesion, promedio in datos_encontrados:
                print(f"{nombre} -- {profesion} -- {promedio}.")
        else:
            print(f"No se encontraron egresados con la profesión {profesion}.")
        return encontrado
    
    def buscar_promedio(self, promedio):
        encontrado = self.arbolpromedio.buscar(promedio)
        if encontrado:
            datos_encontrados = [fila for fila in self.datos_alumnos if fila[2] == promedio]
            for nombre, profesion, promedio in datos_encontrados:
                print(f"{nombre} -- {profesion} -- {promedio}.")
        else:
            print(f"No se encontraron egresados con ese promedio {promedio}.")
        return encontrado
    
    def avanzado_profesion_promedio(self, profesion, promedio):
        datos_encontrados = [fila for fila in self.datos_alumnos if fila[1] == profesion and fila[2] == promedio]
        if len(datos_encontrados) > 0:
            for nombre, profesion, promedio in datos_encontrados:
                print(f"{nombre} -- {profesion} -- {promedio}.")
            return True
        else:
            print(f"No se encontraron egresados con la profesión {profesion} y promedio {promedio}.")
            return False
        
    def imprimir_egresados_nombre(self):
        print("Egresados por nombre:")
        self.arbolnombre.imprimir_en_orden(self.datos_alumnos)
        
    def imprimir_egresados_profesion(self):
        print("Egresados por profesión:")
        self.arbolprofesion.imprimir_en_orden(self.datos_alumnos)
        
    def imprimir_egresados_promedio(self):
        print("Egresados por promedi:")
        self.arbolpromedio.imprimir_en_orden(self.datos_alumnos)
    
if __name__ == '__main__':
    # Carga de datos
    egresados = Egresados('Egresados.csv')
    egresados.cargar_datos()
    
    # Menú de opciones
    while True:
        print("Seleccione una opción:")
        print("1. Buscar egresado por nombre")
        print("2. Buscar egresados por profesión")
        print("3. Buscar egresados por promedio")
        print("4. Buscar egresados por profesión y promedio")
        print("5. Listar Egresados por Nombres")
        print("6. Listar Egresados por Profesión")
        print("7. Listar Egresados por Promedio")
        print("8. Salir")
        opcion = input("Ingrese el número de opción: ")
        print("---------------------------------------------")

        if opcion == "1":
            nombre_buscado = input("Ingrese el nombre del egresado a buscar: ")
            print("---------------------------------------------")
            encontrado = egresados.buscar_nombre(nombre_buscado)
            print("---------------------------------------------")
        elif opcion == "2":
            profesion_buscado = input("Ingrese la profesión de los egresados a buscar: ")
            print("---------------------------------------------")
            encontrado = egresados.buscar_profesion(profesion_buscado)
            print("---------------------------------------------")
        elif opcion == "3":
            promedio_buscado = input("Ingrese el promedio de los egresados a buscar: ")
            print("---------------------------------------------")
            encontrado = egresados.buscar_promedio(promedio_buscado)
            print("---------------------------------------------")
        elif opcion == "4":
            profesion_buscado = input("Ingrese la profesión de los egresados a buscar: ")
            print("---------------------------------------------")
            promedio_buscado = input("Ingrese el promedio de los egresados a buscar: ")
            print("---------------------------------------------")
            egresados.avanzado_profesion_promedio(profesion_buscado, promedio_buscado)
            print("---------------------------------------------")
        elif opcion == "5":
            print("---------------------------------------------")
            egresados.imprimir_egresados_nombre()
            print("---------------------------------------------")
        elif opcion == "6":
            print("---------------------------------------------")
            egresados.imprimir_egresados_profesion()
            print("---------------------------------------------")
        elif opcion == "7":
            print("---------------------------------------------")
            egresados.imprimir_egresados_promedio()
            print("---------------------------------------------")
        elif opcion == "8":
            break
        else:
            print("Opción no válida, intente nuevamente.")
        print()