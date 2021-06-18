import tkinter as tk
from Interfaz.ventana_parametros import v_parametros

class v_main():

    def act_nuevaPartida(self,ventana):
        v_parametro = v_parametros(ventana)
        

    def add_componentes(self,ventana):
        btn_nueva_partida = tk.Button(ventana,text='Nueva Partida',pady=12,padx=20,command=lambda:self.act_nuevaPartida(ventana))
        btn_nueva_partida.pack()
        btn_cargar_partida = tk.Button(ventana,text='Cargar Partida',pady=12,padx=19)
        btn_cargar_partida.pack()
        btn_ayuda = tk.Button(ventana,text='Ayuda',pady=12,padx=40)
        btn_ayuda.pack()
        #btn_ayuda.place(x=150,y=150)

#-----------------------------------------------------------------------
    def centrar(self,root):
        ancho_ventana = 300
        alto_ventana = 200

        x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        root.geometry(posicion)
#--------------------------------------------------------------------------------------
    def __init__(self):
        ventana = tk.Tk()
        ventana.title("Principal")
        ventana.resizable(0,0)
        self.centrar(ventana)
        self.add_componentes(ventana)
        ventana.mainloop()