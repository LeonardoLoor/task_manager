import tkinter as tk
from tkinter import messagebox, simpledialog
from app.gestor_tareas import GestorTareas
from app.tarea import Tarea

class Interfaz:
    def __init__(self, root):
        #Inicializa la interfaz gráfica de la aplicación.
        self.gestor = GestorTareas()
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x700") #tamaño de la ventana
        
        self.frame = tk.Frame(self.root, bg="#1C1C1C")
        self.frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.titulo_label = tk.Label(self.frame, text="Gestor de Tareas", font=("Helvetica", 16, "bold"), bg="#1C1C1C", fg="white")
        self.titulo_label.pack(pady=10)
        
        self.lista_tareas = tk.Listbox(self.frame, width=50, height=10, bg="white", font=("Helvetica", 12, "bold"))
        self.lista_tareas.pack(pady=10, ipady=10)
        
        self.entry_tarea = tk.Entry(self.frame, width=40, font=("Helvetica", 12, "bold"))
        self.entry_tarea.pack(pady=10, ipady=5)
        
        self.boton_agregar = tk.Button(self.frame, text="Agregar Tarea", command=self.agregar_tarea, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"))
        self.boton_agregar.pack(pady=5, fill="x", expand=True)
        
        self.boton_completar = tk.Button(self.frame, text="Completar Tarea", command=self.completar_tarea, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"))
        self.boton_completar.pack(pady=5, fill="x", expand=True)
        
        self.boton_eliminar = tk.Button(self.frame, text="Eliminar Tarea", command=self.eliminar_tarea, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"))
        self.boton_eliminar.pack(pady=5, fill="x", expand=True)
        
        self.boton_editar = tk.Button(self.frame, text="Editar Tarea", command=self.editar_tarea, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"))
        self.boton_editar.pack(pady=5, fill="x", expand=True)
        
        self.boton_filtrar_completadas = tk.Button(self.frame, text="Mostrar Tareas Completadas", command=self.mostrar_completadas, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"))
        self.boton_filtrar_completadas.pack(pady=5, fill="x", expand=True)
        
        self.boton_filtrar_pendientes = tk.Button(self.frame, text="Mostrar Tareas Pendientes", command=self.mostrar_pendientes, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"))
        self.boton_filtrar_pendientes.pack(pady=5, fill="x", expand=True)
        
        self.boton_mostrar_todas = tk.Button(self.frame, text="Mostrar Todas", command=self.actualizar_lista, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"))
        self.boton_mostrar_todas.pack(pady=5, fill="x", expand=True)
        self.actualizar_lista()
    
    def agregar_tarea(self):
        #Agrega una nueva tarea a la lista de tareas.
        descripcion = self.entry_tarea.get()
        if descripcion.strip():
            self.gestor.agregar_tarea(descripcion)
            self.entry_tarea.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "La descripción de la tarea no puede estar vacía.")
    
    def completar_tarea(self):
        #Marca una tarea seleccionada como completada.
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            tarea_id = self.lista_tareas.get(seleccion).split(" ")[0]
            self.gestor.actualizar_tarea(int(tarea_id), True)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para completar.")
    
    def eliminar_tarea(self):
        #Marca una tarea seleccionada como completada.
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            tarea_id = self.lista_tareas.get(seleccion).split(" ")[0]
            self.gestor.eliminar_tarea(int(tarea_id))
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")
    
    def editar_tarea(self):
        #Edita la descripción de una tarea seleccionada.
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            tarea_id = self.lista_tareas.get(seleccion).split(" ")[0]
            nueva_descripcion = simpledialog.askstring("Editar Tarea", "Nueva descripción")
            if nueva_descripcion and nueva_descripcion.strip():
                try:
                    self.gestor.db.cursor.execute('''
                        UPDATE tareas SET descripcion = ? WHERE id = ?
                    ''', (nueva_descripcion, tarea_id))
                    self.gestor.db.connection.commit()
                    self.actualizar_lista()
                except Exception as e:
                    messagebox.showerror("Error", f"Error al editar la tarea: {e}")
                
            else:
                messagebox.showwarning("Advertencia", "La descripción de la tarea no puede estar vacía.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para editar.")
    
    def mostrar_completadas(self):
        #Muestra solo las tareas completadas.
        self.lista_tareas.delete(0, tk.END)
        tareas = self.gestor.obtener_tareas()
        for tarea in tareas:
            if tarea.completada:
                estado = "Completada" if tarea.completada else "Pendiente"
                self.lista_tareas.insert(tk.END, f"{tarea.id} - {tarea.descripcion} [{estado}]")
    
    def mostrar_pendientes(self):
        #Muestra solo las tareas pendientes.
        self.lista_tareas.delete(0, tk.END)
        tareas = self.gestor.obtener_tareas()
        for tarea in tareas:
            if not tarea.completada:
                estado = "Completada" if tarea.completada else "Pendiente"
                self.lista_tareas.insert(tk.END, f"{tarea.id} - {tarea.descripcion} [{estado}]")
    
    def actualizar_lista(self):
        #Actualiza la lista de tareas en la interfaz.
        self.lista_tareas.delete(0, tk.END)
        tareas = self.gestor.obtener_tareas()
        for tarea in tareas:
            estado = "Completada" if tarea.completada else "Pendiente"
            self.lista_tareas.insert(tk.END, f"{tarea.id} - {tarea.descripcion} [{estado}]")

