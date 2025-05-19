#importo el modulo tkinter
import tkinter as tk
import sqlite3

#un comnetario por hacer un cambio 

#creacion/conexion de la base de datos
conn = sqlite3.connect("Jugadores.db")

#creo cursor
cursor = conn.cursor()

#crear tabla para alamacenar datos
cursor.execute('''
               CREATE TABLE IF NOT EXISTS jugadores (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               puntuacion INTEGER DEFAULT 0 
               )
               ''')

#confirmo la creacion de tablas 
conn.commit()

def comenzar_juego():
    nombre = entrada_nombre.get().strip()

    if nombre:
        cursor.execute("INSERT INTO jugadores (nombre, puntuacion) VALUES (?, ?)", (nombre, 0))
        conn.commit() 
        # aquí iría llamada a la siguiente ventana
    else:
        label_mensaje.config(text='Por favor introduce un nombre: ')

#creacion de ventana principal
root = tk.Tk()
root.title('Login del juego')
root.geometry('300x300')

#widgets
label_titulo = tk.Label(root, text='Introduce tu nombre', font=("Elephant", 14))
label_titulo.pack(pady=10)

#cuadro de entrada de texto
entrada_nombre = tk.Entry(root, font=("Elephant", 14))
entrada_nombre.pack()

boton_comenzar = tk.Button(root, text='COMENZAR', font=("Elephant", 14), command=comenzar_juego)
boton_comenzar.pack(pady=10)

#creo un label para informar que no se ha introducido un nombre 
label_mensaje = tk.Label(root, text='', fg='red', font=('Modern', 14))
label_mensaje.pack(pady=10)

root.mainloop()

#modificaria la puntuacion

