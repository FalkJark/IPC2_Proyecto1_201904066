import tkinter as tk
from Interfaz.ventana_main import v_main
from TDAs.mz_ortogonal.matriz_ortogonal import mz_ortogonal
from Interfaz.ventana_tablero import v_tablero
import os
from Interfaz.mostrar_grafo import crear_graphviz
import time
#from Interfaz.crear_img_tablero import crear_tablero


root = v_main()
#v = v_tablero()
#os.system('cls')
#tablero = mz_ortogonal('Prueba',8,8)

#tablero.reemplazar_valor(0,0,'Hola')
#tablero.reemplazar_valor(1,0,'cuadro')
#tablero.reemplazar_valor(2,0,'Manzanosa!')
#crear_graphviz(tablero)
'''
tablero.insertar_pieza(2,2,4,'blue')
tablero.insertar_pieza(4,7,3,'green')
tablero.insertar_pieza(6,2,5,'yellow')
tablero.insertar_pieza(1,3,3,'green')
tablero.insertar_pieza(1,3,4,'green')
#time.sleep(10)
crear_tablero(tablero)
'''
'''
print(tablero.obtener_valor(2,3))
tablero.reemplazar_valor(2,3,'Farik')
print(tablero.obtener_valor(2,3))



print('COLUMNAS: -----')
tablero.mostrar_columna(0)
print('------------')
tablero.mostrar_columna(1)
print('------------')
tablero.mostrar_columna(2)
print('------------')
tablero.mostrar_columna(3)
print('')
print('FILAS: -----')
tablero.mostrar_fila(0)
print('------------')
tablero.mostrar_fila(1)
print('------------')
tablero.mostrar_fila(2)
print('------------')
tablero.mostrar_fila(3)
print('')
tablero.mostrar_fila(4)
print('')
'''
