import tkinter as tk
from tkinter import ttk
from tkinter.constants import Y
#from index import root

class v_parametros():

    def __init__(self,root):
        ventana_parametros = tk.Toplevel(root)
        btn = tk.Button(ventana_parametros,text='regresar',)
        ventana_parametros.title("Principal")
        ventana_parametros.resizable(0,0)
        self.centrar(ventana_parametros)
        self.add_componentes(ventana_parametros)
        root.withdraw()
        ventana_parametros.focus_force()

    def add_componentes(self,ventana):
        lb_title = tk.Label(ventana,text='Parametros de la partida',pady=10)
        lb_title.pack()
        
        lb_p1 = tk.Label(ventana,text='Jugador 1')
        cb_colorP1 = ttk.Combobox(ventana,values=["Azul","Rojo","Amarillo","Verde"])
        cb_colorP1.place(x=25,y=100)
        lb_p1.place(x=25,y=50)
        
        lb_p2 = tk.Label(ventana,text='Jugador 2')
        lb_p2.place(x=200,y=50)
        cb_colorP2 = ttk.Combobox(ventana,values=["Azul","Rojo","Amarillo","Verde"])
        cb_colorP2.place(x=200,y=100)


        lb_x = tk.Label(ventana,text='Columnas:')
        lb_y = tk.Label(ventana,text='Filas:')
        lb_x.place(x=390,y=100)
        lb_y.place(x=390,y=125)

        columnas = tk.StringVar()
        entryX = tk.Entry(ventana, width=4, textvariable=columnas)
        entryX.place(x=490,y=100)

        filas = tk.StringVar()
        entryY = tk.Entry(ventana, width=4, textvariable=filas)
        entryY.place(x=490,y=125)        

        lb_time = tk.Label(ventana,text='tiempo por turno:')
        lb_time.place(x=390,y=150)        

        tiempo = tk.StringVar()
        entryTime = tk.Entry(ventana, width=4, textvariable=tiempo)
        entryTime.place(x=490,y=150)

        lb_tablero = tk.Label(ventana,text='Tablero')
        lb_tablero.place(x=400,y=50)
        
        btn = tk.Button(ventana,text='Empezar')
        btn.place(x=425,y=200)
        #print(comboExample.current(), comboExample.get())
        #btn = tk.Button(ventana,text='xxxx',pady=12,padx=20,command=lambda:print(comboExample.get()))
        #btn.pack()

        ''' btn_nueva_partida = tk.Button(ventana,text='Nueva Partida',pady=12,padx=20,command=self.act_nuevaPartida)
        btn_nueva_partida.pack()
        btn_cargar_partida = tk.Button(ventana,text='Cargar Partida',pady=12,padx=20)
        btn_cargar_partida.pack()
        btn_ayuda = tk.Button(ventana,text='Ayuda',pady=12,padx=20)
        btn_ayuda.pack()
        '''
#-----------------------------------------------------------------------
    def centrar(self,root):
        ancho_ventana = 550
        alto_ventana = 250

        x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        root.geometry(posicion)
