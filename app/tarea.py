class Tarea:
    def __init__(self, descripcion, completada=False, tarea_id=None):
        self.id = tarea_id
        self.descripcion = descripcion
        self.completada = completada
    
    def completar(self):
        self.completada = True
    
    def __repr__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"Tarea(id={self.id}. descripcion='{self.descripcion}', estado={estado})"