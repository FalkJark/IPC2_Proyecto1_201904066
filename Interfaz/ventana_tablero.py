import math
import tkinter as tk
from math import floor
#import Interfaz.pieza_futura as pf
from TDAs.mz_ortogonal.matriz_ortogonal import mz_ortogonal
import db
from Interfaz.mostrar_grafo import crear_graphviz
from Interfaz.crear_img_tablero import crear_tablero
from PIL import Image, ImageTk


class v_tablero():
    def __init__(self,root):
        #global signup_image
        
        ventana_tablero = tk.Toplevel(root)
        ventana_tablero.title("Tablero")
        ventana_tablero.resizable(0,0)
        self.centrar(ventana_tablero)


        #imag1 = Image.open('tablero.gif')
        #img = imag1.resize((550, 400),Image.ANTIALIAS)
        #canvas = tk.Canvas(ventana_tablero, height=500, width=400)
        #signup_image = tk.PhotoImage(file='tablero.gif')
        #signup_image = tk.PhotoImage(img)
        #image2 = canvas.create_image(0, 0, anchor='nw', image=signup_image)
        #canvas.pack(side='top')
        
        

        


        tablero = mz_ortogonal('actual',db.columnas,db.filas)
        crear_tablero(tablero)
        self.add_componentes(ventana_tablero,tablero)
        root.withdraw()
        ventana_tablero.focus_force()
#-----------------------------------------------------------------------
    def centrar(self,root):
        ancho_ventana = 850
        alto_ventana = 500

        x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        root.geometry(posicion)
#-----------------------------------------------------------------------
    def add_componentes(self,ventana,tablero):
        global new_img
        imag1 = Image.open('tablero.gif')
        resized = imag1.resize((550,400),Image.ANTIALIAS)
        new_img = ImageTk.PhotoImage(resized)
        lb_tab = tk.Label(ventana,image=new_img)
        lb_tab.place(x=20,y=20)

        global futura_pieza
        futura_pieza = ImageTk.PhotoImage(file='Imagenes/rec_v.gif')
        lb_tab = tk.Label(ventana,image=futura_pieza)
        lb_tab.place(x=630,y=200)

        lb_x = tk.Label(ventana,text='Columna:')
        lb_y = tk.Label(ventana,text='Fila:')
        lb_x.place(x=20,y=440)
        lb_y.place(x=150,y=440)

        posx = tk.StringVar()
        entryX = tk.Entry(ventana, width=4, textvariable=posx,bg='pink')
        entryX.place(x=85,y=440)

        posy = tk.StringVar()
        entryY = tk.Entry(ventana, width=4, textvariable=posy,bg='pink')
        entryY.place(x=200,y=440)     

        btn_colocar = tk.Button(ventana,text='Colocar')
        btn_colocar.place(x=250,y=440)
        
