class Graduado:
    def __init__(self, indice, nombre, profesion, promedio):
        self.indice = indice
        self.nombre = nombre
        self.profesion = profesion
        self.promedio = promedio

    def get_indice(self):
        return self.indice

    def get_nombre(self):
        return self.nombre

    def get_profesion(self):
        return self.profesion

    def get_promedio(self):
        return self.promedio

    def __str__(self):
        return f"Alumnos: {self.nombre} Profesion: {self.profesion} Con promedio: {self.promedio}"
