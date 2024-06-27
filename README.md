# Gestor de Tareas

Este es un sistema de gestión de tareas desarrollado en Python utilizando `tkinter` para la interfaz gráfica y `sqlite3` para la base de datos.

## Características

- Agregar nuevas tareas
- Eliminar tareas
- Editar descripción de tareas
- Marcar tareas como completadas
- Filtrar tareas por completadas y pendientes
- Interfaz gráfica de usuario

## Estructura del Proyecto
task_manager/
├── app/
│ ├── init.py
│ ├── base_de_datos.py
│ ├── gestor_tareas.py
│ ├── interfaz.py
│ ├── tarea.py
├── database/
│ └── tareas.db
├── tests/
│ ├── init.py
│ └── test_gestor_tareas.py
├── .gitignore
├── README.md
└── main.py


## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tu-usuario/task_manager.git
    ```

2. Navega al directorio del proyecto:
    ```sh
    cd task_manager
    ```

3. Instala las dependencias (si es necesario):
    ```sh
    pip install -r requirements.txt
    ```

## Uso

Para ejecutar la aplicación, utiliza el siguiente comando:

```sh
python main.py

