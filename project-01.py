print("Hola, Bienvenido al Proyecto N°1 de DB3NJA")

Python
import tkinter as tk

def cargar_tareas():
    # Leer el archivo data.txt y devolver la lista de tareas
    pass

def guardar_tareas(tareas):
    # Escribir la lista de tareas en el archivo data.txt
    pass

def agregar_tarea(tarea):
    # Agregar una nueva tarea a la lista y guardarla en el archivo
    pass

def eliminar_tarea(indice):
    # Eliminar una tarea de la lista por su índice y guardarla en el archivo
    pass

def marcar_completada(indice):
    # Marcar una tarea como completada en la lista y guardarla en el archivo
    pass

def mostrar_lista(tareas):
    # Mostrar la lista de tareas pendientes en la interfaz gráfica
    pass

def obtener_accion():
    # Solicitar al usuario una acción (agregar, eliminar, marcar como completada)
    pass

def main():
    # Cargar la lista de tareas al iniciar la aplicación
    tareas = cargar_tareas()

    # Crear la interfaz gráfica y mostrar la lista de tareas
    ventana = tk.Tk()
    mostrar_lista(tareas)

    # Bucle principal
    while True:
        accion = obtener_accion()

        if accion == "agregar":
            nueva_tarea = obtener_nueva_tarea()
            agregar_tarea(nueva_tarea)
            mostrar_lista(tareas)
        elif accion == "eliminar":
            indice = obtener_indice_eliminacion()
            eliminar_tarea(indice)
            mostrar_lista(tareas)
        elif accion == "completar":
            indice = obtener_indice_completar()
            marcar_completada(indice)
            mostrar_lista(tareas)
        elif accion == "salir":
            break

    # Guardar la lista de tareas al cerrar la aplicación
    guardar_tareas(tareas)

    ventana.mainloop()

if __name__ == "__main__":
    main()