import os
import django

# Configura la variable de entorno para la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasKmanager.settings')

# Inicializa Django
django.setup()

# A partir de aquí puedes importar y utilizar los modelos de tu aplicación
from tasks.models import Task  # Asegúrate de ajustar el nombre del modelo según sea necesario

def query_tasks():
    # Consulta todos los objetos de la tabla Task y muestra su información
    tasks = Task.objects.all()
    for task in tasks:
        print(f'Task ID: {task.id}, Title: {task.title}, Completed: {task.completed}')

# Llamada a la función para ejecutar la consulta
if __name__ == '__main__':
    query_tasks()
