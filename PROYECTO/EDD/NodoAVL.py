import NodoAVL

class NodoAVL:
    def __init__(self, indice=None, dato=None, izq:NodoAVL=None, der:NodoAVL=None, padre:NodoAVL=None,f_eq:int=0):
        self.__indice=indice
        self.__dato = dato
        self.__izq = izq
        self.__der = der
        self.__padre = padre
        self.__f_eq = f_eq
        self.datosiguales=[]
    
        
    @property
    def indice(self):
        return self.__indice
    @indice.setter
    def indice(self, indice):
        self.__indice =indice
    @property
    def dato(self):
        return self.__dato
    @dato.setter
    def dato(self, dato):
        self.__dato = dato
    @property
    def izq(self):
        return self.__izq
    @izq.setter
    def izq(self, izq):
        self.__izq=izq
    @property
    def der(self):
        return self.__der
    @der.setter
    def der(self, der):
        self.__der=der

    @property
    def f_eq(self):
        return self.__f_eq
    @f_eq.setter
    def f_eq(self, f_eq):
        self.__f_eq = f_eq

    @property
    def padre(self):
        return self.__padre
    @padre.setter
    def padre(self, padre):
        self.__padre = padre

    @staticmethod
    def altura(nodo:NodoAVL=None)->int:
        if nodo is None:
            return -1
        else:
            return 1 + max(NodoAVL.altura(nodo.izq),NodoAVL.altura(nodo.der))
        
    #Recorridos del árbol
    def inorden(self):
        if self.izq != None:
            self.izq.inorden()
        print(self.dato,"| FE: ",self.f_eq, "Indices", self.indice)
        if self.der != None:
            self.der.inorden()

    def posorden(self):
        if self.izq != None:
            self.izq.posorden()
        if self.der != None:
            self.der.posorden()
        print(self.dato,"| FE: ",self.f_eq)
         
    def preorden(self):
        print(self.dato,"| FE: ",self.f_eq)
        if self.izq != None:
            self.izq.preorden()
        if self.der != None:
            self.der.preorden()
            
            
    def insertar_dato_igual(self, dato, indice):
        self.datosiguales.append((dato, indice))