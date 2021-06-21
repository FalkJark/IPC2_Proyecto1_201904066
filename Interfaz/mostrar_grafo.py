import os 
import subprocess
import webbrowser

def cmd(commando):
    subprocess.run(commando, shell=True)

def crear_graphviz(matriz):
    file = open('matriz.dot','w')
    file.write('digraph matriz_ortogonal{\n')
    nombre = matriz.nombre 
    
    ejex = matriz.derecha
    ejey = matriz.abajo
    headx = ejex.head
    heady = ejey.head
    
    file.write('node [shape=box]\n')

    
    file.write('nodoMain[ label = "'+matriz.nombre+'", width = 1.5, style = filled, fillcolor = firebrick1, group = 1 ];\n')
    
    file.write('''
    e0[ shape = point, width = 0 ];
    e1[ shape = point, width = 0 ];\n
    ''')


    # ---------------------------------Cabeceras y ---------------------------------
    for i in range(ejey.dimension):
        if i == 0:   
            file.write('f0 [label = "0"  pos = "5.3,3.5!",width = 1.5, style = filled, fillcolor = bisque1, group = 1 ];\n')
            heady = heady.abajo
        else:
            file.write('    f'+str(i)+' [label = "'+str(heady.coordenaday)+'" ,  width = 1.5, style = filled, fillcolor = bisque1, group = 1 ];\n')
            heady = heady.abajo


    heady = ejey.head
    for i in range(ejey.dimension-1):
        file.write('    f'+str(i)+'->'+'f'+str(i+1)+'[dir="both"];\n')

    # --------------------------------- Cabeceras x ---------------------------------
    for i in range(ejex.dimension):
        file.write('    c'+str(i)+' [label = "'+str(headx.coordenadax)+'",   width = 1.5, style = filled, fillcolor = lightskyblue, group ='+str(2+i)+'];\n')
        headx = headx.derecha

    headx = ejex.head
    for i in range(ejex.dimension-1):
        file.write('    c'+str(i)+'->'+'c'+str(i+1)+'[dir="both"];\n')


    # --------------------------------- nodo matriz ---------------------------------
    file.write('nodoMain->c0\n')
    file.write('nodoMain->f0\n')

    aux = '{ rank = same;nodoMain;'
    for i in range(ejex.dimension):
        aux = aux +'c'+str(i)+';'
    aux = aux + '}\n \n'
    file.write(aux)

    # crear los nodos matriz
    group = 2
    for j in range(ejey.dimension):
        for i in range(ejex.dimension):
            file.write('n'+str(i)+'_'+str(j)+' [label = "'+str(matriz.obtener_valor(i,j))+'" width = 1.5, group = '+str(group+i)+' ];\n')
            #print(str(i)+','+str(j))

    file.write('\n')
    
    #conectar filas de nodos matriz horizontal
    for j in range(ejey.dimension):
        file.write('f'+str(j)+'->n0_'+str(j)+'[dir="both"];\n')
        for i in range(ejex.dimension-1):
            file.write('n'+str(i)+'_'+str(j)+'->n'+str(i+1)+'_'+str(j)+'[dir="both"];\n')

    file.write('\n')
    
    #alinear filas de nodos matriz horizontal
    for j in range(ejey.dimension):
        aux = '{ rank = same;'
        aux = aux + 'f'+str(j)+';'
        for i in range(ejex.dimension):
            aux = aux + 'n' + str(i) + '_' + str(j) + ';'
        aux = aux + '}\n'
        file.write(aux)

    #conectar filas de nodos matriz vertical
    for j in range(ejex.dimension):
        file.write('c'+str(j)+'->n'+str(j)+'_0 [dir="both"];\n')
        for i in range(ejey.dimension-1):
            file.write('n'+str(j)+'_'+str(i)+'->n'+str(j)+'_'+str(i+1)+'[dir="both"];\n')

    file.write('}')
    file.close()


     #crear archivo pdf
    cmd('dot -Tpdf matriz.dot -o matriz.pdf')

    #abrir pdf con el navegador
    webbrowser.open('matriz.pdf')



