from NodoAVL import *

class ArbolAVL:
    def __init__(self) -> None:
        self.__raiz =None
    
    @property
    def raiz(self):
        return self.__raiz
    @raiz.setter
    def raiz(self,dato):
        self.__raiz=dato

    def inorden(self):
        if self.raiz is not None:
            self.raiz.inorden()
    
    def inordenR(self):
        self.__inorden_recursivo(self.raiz)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izq)
            print(nodo.dato)
            self.__inorden_recursivo(nodo.der)

    #------------------Rotaciones------------------------
    def __rotacion_ii(self, nodo:NodoAVL):
        #Establecer los apuntadores..
        padre = nodo.padre
        p = nodo #Nodo
        q = p.izq #Nodo1
        b = q.der #Hijo derecho de Nodo1

        #Ajustar hijos
        #Al padre de Nodo se le coloca como hijo a Nodo1 en el lugar correspondiente
        if padre is not None:
            if padre.der == p: padre.der = q 
            else: padre.izq = q
        else: self.raiz = q
        #Reconstruir el arbol
        p.izq = b
        q.der = p
        #Reasignar Padres
        p.padre = q
        if b is not None: b.padre = p
        q.padre = padre
        #Establecer el factor de equilibrio
        p.f_eq = 0
        q.f_eq = 0

    def __rotacion_dd(self, nodo:NodoAVL):
        #Establecer los apuntadores..
        padre = nodo.padre
        p = nodo #Nodo
        q = p.der #Nodo1
        b = q.izq #Hijo izquierdo de Nodo1

        #Ajustar hijos
        #Al padre de Nodo se le coloca como hijo a Nodo1 en el lugar correspondiente
        if padre is not None:
            if padre.izq == p: padre.izq = q
            else: padre.der = q
        else: self.raiz = q
        #Reconstruir el arbol
        p.der = b
        q.izq = p

        #Reasignar Padres
        p.padre=q
        if b is not None: b.padre = p
        q.padre = padre
    
        #Establecer el factor de equilibrio
        p.f_eq = 0
        q.f_eq = 0

    def __rotacion_id(self, nodo:NodoAVL):
        padre = nodo.padre
        p = nodo #Nodo
        q = p.izq #Nodo1
        r = q.der #Nodo2
        b = r.izq
        c = r.der
     
        if padre is not None:
            if padre.der == p: padre.der = r
            else: padre.izq = r
        else: self.raiz = r

        #Reconstrucción del árbol
        q.der = b #Colocar el hijo izquierdo de Nodo2 como hijo derecho de Nodo1
        p.izq = c #Colocar el hijo derecho de Nodo2 como hijo izquierdo de Nodo
        #Colocar a Nodo1 y Nodo2 como hijos izquierdo y derecho de Nodo
        r.izq = q
        r.der = p 
        #Reasignación de padres
        r.padre = padre
        p.padre = r
        q.padre = r
        if b is not None: b.padre = q
        if c is not None: c.padre = p
        
        #Ajusta los valores de los factores de equilibrio 
        if r.f_eq == -1: #Nodo2
             p.f_eq = 0 #Nodo
             q.f_eq = 1 #Nodo1
        elif r.f_eq == 0:
            p.f_eq = 0 #Nodo
            q.f_eq = 0 #Nodo1
        elif r.f_eq == 1:
            p.f_eq = -1 #Nodo
            q.f_eq =  0 #Nodo1
        r.f_eq = 0
    
    def __rotacion_di(self, nodo):
        padre = nodo.padre
        p = nodo #Nodo
        q = p.der #Nodo1
        r = q.izq #Nodo2
        b = r.der
        c = r.izq
        
        if padre is not None:
            if padre.izq == p: padre.izq = r
            else: padre.der = r
        else: self.raiz = r
        
        #Reconstrucción del árbol
        q.izq = b #Colocar el hijo derecho de Nodo2 como hijo izquierdo de Nodo1
        p.der = c #Colocar el hijo izquierdo de Nodo2 como hijo derecho de Nodo
        #Colocar a Nodo1 y Nodo2 como hijos izquierdo y derecho de Nodo
        r.der = q
        r.izq = p 
        #Reasignación de padres
        r.padre = padre
        p.padre = r
        q.padre = r
        if b is not None: b.padre = q
        if c is not None: c.padre = p
        
        #Ajusta los valores de los factores de equilibrio 
        if r.f_eq == -1: #Nodo2
             p.f_eq = 0 #Nodo
             q.f_eq = 1 #Nodo1
        elif r.f_eq == 0:
            p.f_eq = 0 #Nodo
            q.f_eq = 0 #Nodo1
        elif r.f_eq == 1:
            p.f_eq = -1 #Nodo
            q.f_eq =  0 #Nodo1
        r.f_eq = 0
    
    def __balancear(self, nodo:NodoAVL):
        fe_actual = nodo.f_eq
        if fe_actual == 2:
            #Determinar la rotación
            fe_hijo_der = nodo.der.f_eq
            if fe_hijo_der == 0:
                pass
            elif fe_hijo_der == 1:
                self.__rotacion_dd(nodo)
                #print("Aplicando rotación DD...")
            elif fe_hijo_der == -1:
                self.__rotacion_di(nodo)
                #print("Aplicando rotación DI...")
        else:
            fe_hijo_izq = nodo.izq.f_eq
            if fe_hijo_izq == 0:
                pass
            elif fe_hijo_izq == -1:
                self.__rotacion_ii(nodo)
                #print("Aplicando rotación II...")
            elif fe_hijo_izq == 1:
                self.__rotacion_id(nodo)
                #print("Aplicando rotación ID...")

    def __recalcular_fe(self, nodo:NodoAVL):
        if nodo is not None:
            nodo.f_eq = NodoAVL.altura(nodo.der)-NodoAVL.altura(nodo.izq)
            if abs(nodo.f_eq) == 2:
                self.__balancear(nodo)
            else:
                self.__recalcular_fe(nodo.padre)

    def buscar_por_profesion(self, profesion):
        nodos_profesion = set()

        def buscar_profesion_recursivo(nodo):
            if nodo is not None:
                if nodo.dato == profesion:
                    nodos_profesion.add(nodo.indice)
                    for dato, indice in nodo.datosiguales:
                        nodos_profesion.add(indice)
                buscar_profesion_recursivo(nodo.izq)
                buscar_profesion_recursivo(nodo.der)

        buscar_profesion_recursivo(self.raiz)
        return nodos_profesion


                
    def __inserta_ordenado(self, nodo, dato, indice):
        n = nodo.dato
        if dato < n:
            if nodo.izq is None:
                nodo.izq = NodoAVL(indice, dato, None, None, nodo)
                self.__recalcular_fe(nodo)
            else:
                self.__inserta_ordenado(nodo.izq, dato, indice)
        elif dato > n:
            if nodo.der is None:
                nodo.der = NodoAVL(indice, dato, None, None, nodo)
                self.__recalcular_fe(nodo)
            else:
                self.__inserta_ordenado(nodo.der, dato, indice)
        else:
            nodo.insertar_dato_igual(dato, indice)
            #print(nodo.datosiguales)

    def listar_ascendente(self):
        datos_ascendentes=[]
        self.__recorrido_ascendente(self.raiz, datos_ascendentes)
        return datos_ascendentes
                
    def __recorrido_ascendente(self, nodo, datos):
        if nodo is not None:
            self.__recorrido_ascendente(nodo.izq, datos)
            datos.append(nodo.indice)
            
            if nodo.datosiguales is not None:
                for dato, indice in nodo.datosiguales:
                    datos.append(indice)
                
            self.__recorrido_ascendente(nodo.der, datos)
            
    def listar_descendente(self):
        datos_descendentes = []
        self.__recorrido_descendente(self.raiz, datos_descendentes)
        return datos_descendentes

    def __recorrido_descendente(self, nodo, datos):
        if nodo is not None:
            self.__recorrido_descendente(nodo.der, datos)
            datos.append(nodo.indice)
        
            if nodo.datosiguales is not None:
                for dato, indice in nodo.datosiguales:
                    datos.append(indice)
        
            self.__recorrido_descendente(nodo.izq, datos)
            
    def insertar(self, dato, indice):
        if self.raiz is None:
            self.__raiz=NodoAVL(indice, dato, None, None,None)
        else:
            self.__inserta_ordenado(self.raiz,dato,indice)

if __name__ == '__main__':
    nodo=NodoAVL()
    arbol = ArbolAVL()
    arbol.insertar(43,1)
    arbol.insertar(75,2)
    arbol.insertar(86,3)
    arbol.insertar(65,4)
    arbol.insertar(65,5)
    arbol.inorden()
    arbol.insertar(70,6)
    arbol.insertar(67,7)
    arbol.insertar(73,8)
    arbol.insertar(93,9)
    arbol.insertar(93,10)
    arbol.insertar(93,11)
    arbol.insertar(69,12)
    arbol.insertar(25,13)
    arbol.insertar(66,14)
    arbol.insertar(68,15)
    arbol.insertar(47,16)
    arbol.insertar(62,17)
    arbol.insertar(10,18)
    arbol.insertar(60,19)
    arbol.insertar(1000,20)   
    arbol.insertar(1000,21)
    arbol.insertar(1000,22)
    arbol.inorden()
    print(arbol.buscar_por_profesion(65))
    
    
    
    
    