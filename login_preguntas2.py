#importo modulos 
import tkinter as tk
import sqlite3

# Conexión a la base de datos (o creación si no existe)
conexion = sqlite3.connect("Jugadores.db")
cursor = conexion.cursor()

# Crear la tabla si aún no está creada
cursor.execute('''
    CREATE TABLE IF NOT EXISTS jugadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    )
''')
conexion.commit()

# lista de Preguntas del juego
cuestionario = [
    {
        "pregunta": "¿Cuál es la capital de Portugal?",
        "opciones": {"A": "Madrid", "B": "Lisboa", "C": "Dublín"},
        "correcta": "B"
    },
    {
        "pregunta": "¿Cuánto es 5 + 7?",
        "opciones": {"A": "10", "B": "11", "C": "12"},
        "correcta": "C"
    },
    {
        "pregunta": "¿Cuál es el color del cielo?",
        "opciones": {"A": "Azul", "B": "Verde", "C": "Rojo"},
        "correcta": "A"
    }
]

# funcion que se ejecuta Al pulsar el botón para comenzar
def iniciar_juego():
    jugador = entrada_nombre.get().strip()

    if jugador:
        cursor.execute("INSERT INTO jugadores (nombre) VALUES (?)", (jugador,))
        #confirmo los cambios 
        conexion.commit()
        #para cerrar la ventana del inicio 
        ventana_inicio.destroy()
        #para comenzar en la pregunta 1
        lanzar_pregunta(jugador, 0)
    else:
        aviso.config(text="Debes ingresar tu nombre")

# funcion para Mostrar cada pregunta del cuestionario 
def lanzar_pregunta(jugador, num):
    if num >= len(cuestionario):
        mostrar_final(jugador)
        return

    pregunta_actual = cuestionario[num]
    #creamos nueva ventana para que se muestre la pregunta 
    ventana_pregunta = tk.Tk()
    ventana_pregunta.title(f"Pregunta {num + 1}")
    ventana_pregunta.geometry("500x300")

#muestro el texto de la pregnta 
    tk.Label(ventana_pregunta, text=pregunta_actual["pregunta"], font=('Calibri', 14)).pack(pady=20)

#funcion para comprobar la respuesta cunado el jugador selecciona una opcion 
    def comprobar(respuesta):
        ventana_pregunta.destroy()
        #suma 1 para pasar a la siguiente pregunta 
        lanzar_pregunta(jugador, num + 1)

#botones para cada opcion 
    for clave, texto in pregunta_actual["opciones"].items():
        tk.Button(ventana_pregunta, text=texto, font=("Calibri", 12),
                  command=lambda eleccion=clave: comprobar(eleccion)).pack(pady=5)

# funcion para Mostrar ventana final
def mostrar_final(jugador):
    ventana_resultado = tk.Tk()
    ventana_resultado.title("Fin del juego")
    ventana_resultado.geometry("400x200")

    #funcion para mostrar mensaje de despedidda 
    tk.Label(ventana_resultado, text=f"Gracias por jugar, {jugador}!", font=("Arial", 16)).pack(pady=30)
    #boton para cerrar ventana
    tk.Button(ventana_resultado, text="Salir", font=("Arial", 12), command=ventana_resultado.destroy).pack()

# Ventana inicial
ventana_inicio = tk.Tk()
ventana_inicio.title("Bienvenido")
ventana_inicio.geometry("300x300")

#para escribir el nombre de cada jugador 
tk.Label(ventana_inicio, text="Nombre del jugador", font=("Calibri", 14)).pack(pady=10)

entrada_nombre = tk.Entry(ventana_inicio, font=("Calibri", 14))
entrada_nombre.pack()

#boton para iniciar el cuetionario 
tk.Button(ventana_inicio, text="Iniciar", font=("Calibri", 14), command=iniciar_juego).pack(pady=10)



aviso = tk.Label(ventana_inicio, text="", fg="red", font=("Arial", 12))
aviso.pack(pady=10)

#iniciar el buclwe principal de la interfaz
ventana_inicio.mainloop()
