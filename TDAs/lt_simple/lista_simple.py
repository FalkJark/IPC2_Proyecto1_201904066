from TDAs.lt_simple.nodo_lista import nodo_simple

class lista_simple():
    def __init__(self):
        self.head = None
        self.dimension = 0

    def agregar(self,valor):
        aux = self.head
        nuevo_nodo = nodo_simple(valor)
        if aux == None:
            self.head = nuevo_nodo
        else:
            while aux.derecha != None:
                aux = aux.derecha
            aux.derecha = nuevo_nodo

    def mostrar(self):
        aux = self.head
        if aux == None:
            print('la lista esta vacia')
        else:
            while aux != None:
                print(str(aux.valor),end='->')
                aux = aux.derecha
            print('null')
