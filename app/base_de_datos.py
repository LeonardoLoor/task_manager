import sqlite3

class BaseDeDatos:
    def __init__(self, db_name="database/tareas.db"):
        #realizamos la conexion con la base de datos = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.crear_tabla()
        
    def crear_tabla(self):
        try:
            self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS tareas (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    descripcion TEXT NOT NULL,
                                    completada BOOLEAN NOT NULL
                                )
                                ''')
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")
    
    def agregar_tarea(self, descripcion, completada=False):
        try:
            self.cursor.execute('''
                                INSERT INTO tareas (descripcion, completada) VALUES (?,?)
                                ''', (descripcion, completada))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error al agregar la tarea: {e}")
    
    def obtener_tareas(self):
        try:
            self.cursor.execute('SELECT * FROM tareas')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al obtener las tareas: {e}")
            return []
    
    def actualizar_tareas(self, tarea_id, completada):
        try:
            self.cursor.execute('''
                                UPDATE tareas SET completada = ? WHERE id = ?
                                ''', (completada, tarea_id))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error al actualizar la tarea: {e}")
    
    def eliminar_tarea(self, tarea_id):
        try:
            self.cursor.execute('DELETE FROM tareas WHERE id = ?', (tarea_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error al eliminar las tareas: {e}")
    
    def cerrar(self):
        self.connection.close()