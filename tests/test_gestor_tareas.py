import unittest
from app.gestor_tareas import GestorTareas
from app.tarea import Tarea

class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorTareas()
        self.gestor.db.cursor.execute('DELETE FROM tareas') #Limpiar la base de datos antes de cada prueba
        self.gestor.db.connection.commit()
    
    def tearDown(self):
        self.gestor.db.cursor.execute('DELETE FROM tareas') #Limpiar la base de datos despues de cada prueba
        self.gestor.db.connection.commit()
    
    def test_agregar_tarea(self):
        self.gestor.agregar_tarea("Tarea de prueba")
        tareas = self.gestor.obtener_tareas()
        self.assertEqual(len(tareas), 1)
        self.assertEqual(tareas[0].descripcion, "Tarea de prueba")
    
    def test_completar_tarea(self):
        self.gestor.agregar_tarea("Tarea de prueba")
        tarea = self.gestor.obtener_tareas()[0]
        self.gestor.actualizar_tarea(tarea.id, True)
        tarea_actualizada = self.gestor.obtener_tareas()[0]
        self.assertTrue(tarea_actualizada.completada)
    
    def test_eliminar_tarea(self):
        self.gestor.agregar_tarea("Tarea de prueba")
        tarea = self.gestor.obtener_tareas()[0]
        self.gestor.eliminar_tarea(tarea.id)
        tareas = self.gestor.obtener_tareas()
        self.assertEqual(len(tareas), 0)


if __name__ == "__main__":
    unittest.main()