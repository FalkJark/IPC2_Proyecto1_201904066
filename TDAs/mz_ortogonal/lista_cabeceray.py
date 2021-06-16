class nodo_cabeceray():
    def __init__(self,coordenada):
        self.coordenaday = coordenada
        self.derecha = None
        self.abajo = None

class lista_cabeceray():
    def __init__(self):
        self.head = None
        self.dimension = 0

    def llenar_listay(self,numero_nodos):
        for i in range(int(numero_nodos)):
            nodo_aux = nodo_cabeceray(i)
            if self.head == None:
                self.head = nodo_aux
                self.dimension += 1
            else:
                ultimo = self.head
                while ultimo.abajo != None:
                    ultimo = ultimo.abajo
                ultimo.abajo = nodo_aux
                self.dimension += 1

    def mostrar_listay(self):
        if self.head == None:
            print('Lista vacia')
            return
        else:
            ultimo = self.head
            while ultimo != None:
                #print(ultimo.coordenaday, end='->')
                print('posY: '+str(ultimo.coordenaday)+', derecha: '+str(ultimo.derecha)+', abajo: '+str(ultimo.abajo))
                ultimo = ultimo.abajo
            print('null')