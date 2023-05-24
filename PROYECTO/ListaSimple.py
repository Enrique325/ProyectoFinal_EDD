

class ListaSimple():
    
    def __init__(self):
        self.primero=None
    
    def insertar_inicio(self,dato):
        nuevo_nodo=NodoLista(dato)
        if self.primero is None:
            self.primero=nuevo_nodo
        else:
            actual=self.primero
            while actual.siguiente is not None:
                actual=actual.siguiente
            actual.siguiente=nuevo_nodo
            
    def buscar(self,dato):
        actual=self.primero
        while actual is not None:
            if actual.dato==dato:
                return actual
            actual=actual.siguiente
        return None
        