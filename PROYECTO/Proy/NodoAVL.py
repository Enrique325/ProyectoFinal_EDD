import NodoAVL

class NodoAVL:
    def __init__(self, dato=None, izq=None, der=None, padre=None, f_eq=0):
        self.__dato = dato
        self.__izq = izq
        self.__der = der
        self.__padre = padre
        self.__f_eq = f_eq

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
        self.__izq = izq
        
    @property
    def der(self):
        return self.__der
    
    @der.setter
    def der(self, der):
        self.__der = der
        
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
        
    @property
    def string(self):
        return self.__string
    
    @string.setter
    def string(self, string):
        self.__string = string
        
    @staticmethod
    def altura(nodo=None):
        if nodo is None:
            return -1
        else:
            return 1 + max(NodoAVL.altura(nodo.izq),NodoAVL.altura(nodo.der))
        
    #Recorridos del árbol
    def inorden(self):
        if self.izq is not None:
            self.izq.inorden()
        print(self.dato,"| FE: ",self.f_eq)
        if self.der is not None:
            self.der.inorden()
            
    def posorden(self):
        if self.izq is not None:
            self.izq.posorden()
        if self.der is not None:
            self.der.posorden()
        print(self.dato,"| FE: ",self.f_eq)
        
    def preorden(self):
        print(self.dato,"| FE: ",self.f_eq)
        if self.izq is not None:
            self.izq.preorden()
        if self.der is not None:
            self.der.preorden()