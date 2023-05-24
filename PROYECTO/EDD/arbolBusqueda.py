import arbolPromedio as arbolpromedios
import arbolProfesion as arbolProfesion

class ArbolAVL():
    arbolPromedi = arbolpromedios.ArbolAVL()
    arbolProfesion = arbolProfesion.ArbolAVL()
    
    def busqueda_inorden_avl_profesion(self, indice_buscado):
        return self.__busqueda_inorden_avl(arbolProfesion.ArbolAVL.raiz, indice_buscado)

    def __busqueda_inorden_avl(self, nodo:NodoAVl(), indice_buscado):
        if nodo is None:
            return None
        
        resultado = self.__busqueda_inorden_avl(nodo.izq, indice_buscado)
        if resultado is not None:
            return resultado

        if isinstance(nodo.dato, list):
            for dato in nodo.dato:
                if dato.indice == indice_buscado:
                    return dato.dato

        resultado = self.__busqueda_inorden_avl(nodo.der, indice_buscado)
        if resultado is not None:
            return resultado

        return None
