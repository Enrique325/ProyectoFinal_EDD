from NodoAVL import *
class ArbolAVL:
    def __init__(self,dato=None) -> None:
        self.__raiz = NodoAVL(dato=dato)
        
    @property
    def raiz(self):
        return self.__raiz
    
    @raiz.setter
    def raiz(self,dato):
        self.__raiz=dato
        
    def inorden(self):
        if self.raiz is not None:
            self.raiz.inorden()
    
    """""
    def agregar(self, indice, dato):
        self.raiz = self._agregar(self.raiz, indice, dato)

    def _agregar(self, nodo, indice, dato):
        if nodo is None:
            return NodoAVL(indice, dato)

        if indice < nodo.indice:
            nodo.izq = self._agregar(nodo.izq, indice, dato)
        else:
            nodo.der = self._agregar(nodo.der, indice, dato)

        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))

        balance = self.__balancear

        if balance > 1 and indice < nodo.izq.indice:
            return self._rotar_derecha(nodo)

        if balance < -1 and indice > nodo.der.indice:
            return self._rotar_izquierda(nodo)

        if balance > 1 and indice > nodo.izq.indice:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo)

        if balance < -1 and indice < nodo.der.indice:
            nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo)

        return nodo


    def buscar(self, nombre):
        nodo = self._buscar(self.raiz, nombre)
        if nodo is None:
            return None
        else:
            return nodo.dato

    def _buscar(self, nodo, nombre):
        if nodo is None or nodo.nombre == nombre:
            return nodo

        if nombre < nodo.nombre:
            return self._buscar(nodo.izq, nombre)
        else:
            return self._buscar(nodo.der, nombre)
        
    """    
    #------------------------------------------------------------------
        
    def convertir_a_indice_alfanumerico(self, numero):
        indice_alfanumerico = ""
        letras = "abcdefghijklmnopqrstuvwxyz"
        while numero > 0:
            resto = (numero - 1) % 26
            indice_alfanumerico = letras[resto] + indice_alfanumerico
            numero = (numero - resto) // 26
        return indice_alfanumerico

    """""
    def agregar(self, dato):
        self.raiz = self.agregar_recursivo(dato, self.raiz)

    def agregar_recursivo(self, dato, nodo):
        if nodo is None:
            self.indice_actual += 1
            indice_actual_str = self.convertir_a_indice_alfanumerico(self.indice_actual)
            return NodoAVL(dato=dato, indice=indice_actual_str)
        
        if dato < nodo.dato:
            nodo.izq = self.agregar_recursivo(dato, nodo.izq)
            nodo.izq.padre = nodo
        else:
            nodo.der = self.agregar_recursivo(dato, nodo.der)
            nodo.der.padre = nodo
        
        nodo.f_eq = self.calcular_factor_equilibrio(nodo)

        if nodo.f_eq == 2:
            if nodo.der.f_eq == -1:
                nodo.der = self.rotar_derecha(nodo.der)
            return self.rotar_izquierda(nodo)
        elif nodo.f_eq == -2:
            if nodo.izq.f_eq == 1:
                nodo.izq = self.rotar_izquierda(nodo.izq)
            return self.rotar_derecha(nodo)
        
        return nodo
        """
        
    def agregar(self, dato):
        self.raiz = self.agregar_recursivo(dato, self.raiz)

    def agregar_recursivo(self, dato, nodo):
        if nodo is None:
            self.indice_actual += 1
            indice_actual_str = self.convertir_a_indice_alfanumerico(self.indice_actual)
            return NodoAVL(dato=dato, indice=indice_actual_str)
        
        if dato.dato < nodo.dato:
            nodo.izq = self.agregar_recursivo(dato, nodo.izq)
            nodo.izq.padre = nodo
        else:
            nodo.der = self.agregar_recursivo(dato, nodo.der)
            nodo.der.padre = nodo
        
        nodo.f_eq = self.calcular_factor_equilibrio(nodo)

        if nodo.f_eq == 2:
            if nodo.der.f_eq == -1:
                nodo.der = self.rotar_derecha(nodo.der)
            return self.rotar_izquierda(nodo)
        elif nodo.f_eq == -2:
            if nodo.izq.f_eq == 1:
                nodo.izq = self.rotar_izquierda(nodo.izq)
            return self.rotar_derecha(nodo)
        
        return nodo
        
    def buscar(self, nombre):
        nodo = self.raiz
        while nodo is not None and nodo.dato != nombre:
            if nombre < nodo.dato:
                nodo = nodo.izq
            else:
                nodo = nodo.der
        return


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
        p = nodo #Nodoa
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
                print("Aplicando rotación DD...")
            elif fe_hijo_der == -1:
                self.__rotacion_di(nodo)
                print("Aplicando rotación DI...")
        else:
            fe_hijo_izq = nodo.izq.f_eq
            if fe_hijo_izq == 0:
                pass
            elif fe_hijo_izq == -1:
                self.__rotacion_ii(nodo)
                print("Aplicando rotación II...")
            elif fe_hijo_izq == 1:
                self.__rotacion_id(nodo)
                print("Aplicando rotación ID...")
                
    def __recalcular_fe(self, nodo:NodoAVL):
        if nodo is not None:
            nodo.f_eq = NodoAVL.altura(nodo.der)-NodoAVL.altura(nodo.izq)
            if abs(nodo.f_eq) == 2:
                self.__balancear(nodo)
            else:
                self.__recalcular_fe(nodo.padre)
                
    def __inserta_ordenado(self, nodo:NodoAVL,dato):
        #if type(nodo.dato) is not int: n = nodo.dato.dato
        n = nodo.dato
        if dato < n:
            if nodo.izq is None:
                nodo.izq = NodoAVL(dato,None,None,nodo)
                self.__recalcular_fe(nodo)
            else:
                self.__inserta_ordenado(nodo.izq,dato)
        elif dato > n:
            if nodo.der is None:
                nodo.der = NodoAVL(dato,None,None, nodo)
                self.__recalcular_fe(nodo)
            else:
                self.__inserta_ordenado(nodo.der,dato)
                
    def insertar(self, dato):
        self.__inserta_ordenado(self.raiz,dato)