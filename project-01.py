import os
os.system("cls")
import tkinter as tk
def cargar_tareas():
    """Lee el archivo data.txt y devuelve una lista de tareas."""
    try:
        with open("data.txt", "r") as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        return []

def guardar_tareas(tareas):
    """Escribe la lista de tareas en el archivo data.txt."""
    with open("data.txt", "w") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")

def agregar_tarea():
    """Agrega una nueva tarea a la lista y actualiza la interfaz."""
    nueva_tarea = entrada_tarea.get()
    if nueva_tarea:
        tareas.append(nueva_tarea)
        guardar_tareas(tareas)
        mostrar_lista(tareas)
        entrada_tarea.delete(0, tk.END)

def eliminar_tarea():
    """Elimina la tarea seleccionada de la lista."""
    indice = lista_tareas.curselection()
    if indice:
        indice = indice[0]
        del tareas[indice]
        guardar_tareas(tareas)
        mostrar_lista(tareas)

def marcar_completada():
    """Marca la tarea seleccionada como completada."""
    # Implementa la lógica para marcar tareas como completadas
    # Por ejemplo, puedes agregar un prefijo "*" a las tareas completadas
    indice = lista_tareas.curselection()
    if indice:
        indice = indice[0]
        tareas[indice] = f"* {tareas[indice]}"
        guardar_tareas(tareas)
        mostrar_lista(tareas)

def mostrar_lista(tareas):
    """Muestra la lista de tareas en la interfaz."""
    lista_tareas.delete(0, tk.END)
    for tarea in tareas:
        lista_tareas.insert(tk.END, tarea)

# Cargar las tareas al iniciar la aplicación
tareas = cargar_tareas()

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Lista de tareas
lista_tareas = tk.Listbox(ventana)
lista_tareas.pack()

# Campo de entrada para la nueva tarea
entrada_tarea = tk.Entry(ventana)
entrada_tarea.pack()

# Botón para agregar la tarea
boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack()

# Botón para eliminar la tarea
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack()

# Botón para marcar como completada
boton_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
boton_completar.pack()

# Mostrar la lista inicial
mostrar_lista(tareas)

ventana.mainloop()