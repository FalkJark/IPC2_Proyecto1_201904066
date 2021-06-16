#---------------------------- EJE X

class nodo_cabecerax():
    def __init__(self,coordenada):
        self.coordenadax = coordenada
        self.derecha = None
        self.abajo = None

class lista_cabecerax():
    def __init__(self):
        self.head = None
        self.dimension = 0

    def llenar_listax(self,numero_nodos):
        for i in range(int(numero_nodos)):
            nodo_aux = nodo_cabecerax(i)
            if self.head == None:
                self.head = nodo_aux
            else:
                #print('pasa por el else')
                ultimo = self.head
                while ultimo.derecha != None:
                    ultimo = ultimo.derecha
                ultimo.derecha = nodo_aux
            self.dimension += 1

    def mostrar_listax(self):
        if self.head == None:
            print('Lista vacia')
            return
        else:
            ultimo = self.head
            while ultimo != None:
                #print(ultimo.coordenadax, end='->')
                print('posX: '+str(ultimo.coordenadax)+', derecha: '+str(ultimo.derecha)+', abajo: '+str(ultimo.abajo))
                ultimo = ultimo.derecha
            print('null')