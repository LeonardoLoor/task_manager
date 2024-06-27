from app.base_de_datos import BaseDeDatos
from app.tarea import Tarea

class GestorTareas:
    def __init__(self):
        self.db = BaseDeDatos()
    
    def agregar_tarea(self, descripcion):
        self.db.agregar_tarea(descripcion)
    
    def obtener_tareas(self):
        tareas_db = self.db.obtener_tareas()
        return [Tarea(tarea[1], tarea[2], tarea[0]) for tarea in tareas_db]
    
    def actualizar_tarea(self, tarea_id, completada):
        self.db.actualizar_tareas(tarea_id, completada)
    
    def eliminar_tarea(self, tarea_id):
        self.db.eliminar_tarea(tarea_id)