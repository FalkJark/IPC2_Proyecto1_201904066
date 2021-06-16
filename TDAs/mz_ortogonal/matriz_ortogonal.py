from TDAs.mz_ortogonal import lista_cabecerax as lx,lista_cabeceray as ly

class nodo_matriz():
    def __init__(self,valor,x,y):
        self.valor = valor
        self.posx = x
        self.posy = y
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None


class mz_ortogonal():

    def __init__(self,tamx,tamy):
        listax = lx.lista_cabecerax()
        listay = ly.lista_cabeceray()

        listax.llenar_listax(tamx)
        listay.llenar_listay(tamy)
        
        self.derecha = listax
        self.abajo = listay

        self.llenar_matriz()

    def mostrar_columna(self,col):
        headx = self.derecha.head
        tamx = self.derecha.dimension

        if int(col) > tamx-1 or int(col) < 0:
            print('La columna no existe')
        else:
            while int(headx.coordenadax) != col:
                headx = headx.derecha

            headx = headx.abajo
            while headx != None:
                #print('valor: '+str(headx.valor)+', x: '+str(headx.posx)+', y: '+str(headx.posy)) 
                print('('+str(headx.posx)+','+str(headx.posy)+') = '+str(headx.valor))
                headx = headx.abajo

    def mostrar_fila(self,fila):
        heady = self.abajo.head
        tamy = self.abajo.dimension

        if int(fila) > tamy-1 or int(fila) < 0:
            print('La fila no existe')
        else:
            while int(heady.coordenaday) != fila:
                heady = heady.abajo

            heady = heady.derecha
            while heady != None:
                print('('+str(heady.posx)+','+str(heady.posy)+') = '+str(heady.valor)) 
                heady = heady.derecha



    def llenar_matriz(self):
        #Valores
        ejex = self.derecha
        ejey = self.abajo
        tamx = ejex.dimension
        tamy = ejey.dimension 

        # PASO 1: crear listas hacia abajo de los nodos del eje x
        contx = 0
        conty = 0
        headx = self.derecha.head
        heady = self.abajo.head
        anteriorx = None
        while headx != None:
            #print('iteracion while')
            #print('headx= '+str(headx.coordenadax))
            headx_abajo = headx
            conty = 0
            for i in range(tamy):
                #print('i= '+str(i))
                nodo_nuevo = nodo_matriz(str(contx+conty),headx.coordenadax,conty)
                if i == 0:
                    nodo_nuevo.arriba = headx_abajo
                    anteriorx = headx_abajo
                else:
                    nodo_nuevo.arriba = anteriorx.abajo
                    anteriorx = anteriorx.abajo
                    #anteriorx.abajo = nodo_nuevo
                headx_abajo.abajo = nodo_nuevo
                headx_abajo = headx_abajo.abajo
                conty += 1
            contx += 1
            headx = headx.derecha

        # PASO 2: Conectar la primera columna con el eje de las Y's
        headx = self.derecha.head
        pivotex = headx.abajo
        print('primer nodo: '+str(pivotex.valor))
        heady = self.abajo.head
        while pivotex != None:
            print('posY: '+str(heady.coordenaday)+', pivote: '+str(pivotex.valor))
            heady.derecha = pivotex
            pivotex.izquierda = heady
            pivotex = pivotex.abajo
            heady = heady.abajo

        # PASO 3: Conectar todos los nodos matriz entre si de forma horizontal
        headx = self.derecha.head
        heady = self.abajo.head

        head_sig = headx.derecha
        while head_sig != None:
            headx2 = headx.abajo
            head_sig2 = head_sig.abajo

            for i in range(int(tamy)):
                headx2.derecha = head_sig2
                head_sig2.izquierda = headx2
                head_sig2 = head_sig2.abajo
                headx2 = headx2.abajo
            headx = headx.derecha
            head_sig = head_sig.derecha