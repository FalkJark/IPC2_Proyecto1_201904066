import tkinter as tk
from tkinter import messagebox, ttk
from Interfaz.ventana_tablero import v_tablero
import db

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
#*********************************************************************************
    def abrir_ventana_tablero(self,ventana):
        v_tab = v_tablero(ventana)

#----------------------------------------------------------------    
    def acciones(self,cb1,cb2,filas,columnas,tiempo,ventana):
        p1= cb1.get()
        p2= cb2.get()
        
        if p1 == "" or p2 == "":
            messagebox.showinfo('Dato erroneo','debes elegir un color por jugador')
        elif p1 == p2:
            messagebox.showinfo('Dato erroneo','los jugadores deben tener colores distintos')
        elif filas == '' or columnas == '' or tiempo == '':
            messagebox.showinfo('Dato Vacio','llena todos los campos del tablero')
        else:
            try:
                tiempo = int(tiempo.get())
                filas = int(filas.get())
                columnas = int(columnas.get())
                print('entra al try')
                
                if tiempo<15 or tiempo>60:
                    messagebox.showinfo('Exceso','el tiempo no puede ser mayor de 60 y menor de 15 seg')
                else:
                    if int(filas)<4 or int(columnas)<4:
                        messagebox.showinfo('Error Dimensiones','el tablero debe tener una dimension minima de 4x4')
                    else:
                        db.filas = filas
                        db.columnas = columnas
                        db.tiempo = tiempo
                        db.p1 = p1.lower()
                        db.p2 = p2.lower()
                        self.abrir_ventana_tablero(ventana)
            except:
                print('entra al except')
                messagebox.showinfo('Dato Erroneo','los parametros del tablero deben ser numeros')
            
#----------------------------------------------------------------------------------------------
    def add_componentes(self,ventana):
        lb_title = tk.Label(ventana,text='Parametros de la partida',pady=10)
        lb_title.pack()
        
        lb_p1 = tk.Label(ventana,text='Jugador 1')
        cb_colorP1 = ttk.Combobox(ventana,values=["Azul","Rojo","Amarillo","Verde"],state="readonly")
        cb_colorP1.place(x=25,y=100)
        lb_p1.place(x=25,y=50)
        
        lb_p2 = tk.Label(ventana,text='Jugador 2')
        lb_p2.place(x=200,y=50)
        cb_colorP2 = ttk.Combobox(ventana,values=["Azul","Rojo","Amarillo","Verde"],state="readonly")
        cb_colorP2.place(x=200,y=100)


        lb_x = tk.Label(ventana,text='Columnas:')
        lb_y = tk.Label(ventana,text='Filas:')
        lb_x.place(x=360,y=100)
        lb_y.place(x=360,y=125)

        columnas = tk.StringVar()
        entryX = tk.Entry(ventana, width=4, textvariable=columnas)
        entryX.place(x=490,y=100)

        filas = tk.StringVar()
        entryY = tk.Entry(ventana, width=4, textvariable=filas)
        entryY.place(x=490,y=125)        

        lb_time = tk.Label(ventana,text='tiempo por turno (seg):')
        lb_time.place(x=360,y=150)        

        tiempo = tk.StringVar()
        entryTime = tk.Entry(ventana, width=4, textvariable=tiempo)
        entryTime.place(x=490,y=150)

        lb_tablero = tk.Label(ventana,text='Tablero')
        lb_tablero.place(x=400,y=50)
        
        btn = tk.Button(ventana,text='Empezar',command=lambda:self.acciones(cb_colorP1,cb_colorP2,entryX,entryY,entryTime,ventana))
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
