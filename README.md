# Gestor de Tareas con Python y PostgreSQL

Aplicación de consola desarrollada en Python para gestionar tareas almacenadas en una base de datos PostgreSQL.

Este proyecto forma parte de mi aprendizaje y práctica de desarrollo con Python, centrándome en la conexión con bases de datos, programación orientada a objetos, operaciones CRUD, validación de datos y organización del código en diferentes módulos.

## Funcionalidades

La aplicación permite:

- Mostrar todas las tareas.
- Buscar una tarea por su ID.
- Crear nuevas tareas.
- Modificar tareas existentes.
- Marcar tareas como completadas.
- Eliminar tareas.
- Mostrar únicamente las tareas pendientes.
- Consultar estadísticas de tareas completadas y pendientes.
- Asignar prioridades: alta, media o baja.
- Validar los datos introducidos por el usuario.
- Gestionar errores de conexión con PostgreSQL.

## Tecnologías utilizadas

- Python
- PostgreSQL
- Psycopg
- python-dotenv
- Git

## Estructura del proyecto

```text
gestor-tareas-python/
│
├── conexion.py
├── main.py
├── menu.py
├── tarea.py
├── tareas.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

### Archivos principales

**main.py**  
Contiene el bucle principal de la aplicación y gestiona las opciones seleccionadas por el usuario.

**menu.py**  
Contiene el menú de opciones mostrado en consola.

**tarea.py**  
Define la clase `Tarea`, utilizada para representar las tareas de la aplicación.

**tareas.py**  
Contiene la lógica principal para crear, consultar, modificar, completar y eliminar tareas, además de los filtros y estadísticas.

**conexion.py**  
Gestiona la conexión con PostgreSQL utilizando variables de entorno.

## Base de datos

El proyecto utiliza una base de datos PostgreSQL llamada:

```text
gestor_tareas
```

La tabla utilizada puede crearse con:

```sql
CREATE TABLE tareas (
    id SERIAL PRIMARY KEY,
    titulo TEXT NOT NULL,
    descripcion TEXT,
    prioridad TEXT,
    completada BOOLEAN DEFAULT FALSE
);
```

## Instalación

Clona el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd gestor-tareas-python
```

Crea un entorno virtual:

```bash
python -m venv .venv
```

Actívalo en Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Configuración

El proyecto utiliza variables de entorno para evitar guardar las credenciales de PostgreSQL directamente en el código.

Crea un archivo `.env` a partir de `.env.example` y configura tus datos:

```env
DB_NAME=gestor_tareas
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
```

El archivo `.env` está excluido del repositorio mediante `.gitignore`.

## Ejecución

Con PostgreSQL iniciado y la base de datos configurada:

```bash
python main.py
```

La aplicación mostrará un menú desde el que se pueden realizar las diferentes operaciones.

## Conceptos practicados

Durante el desarrollo de este proyecto he trabajado especialmente con:

- Programación orientada a objetos.
- Modularización de código en Python.
- PostgreSQL desde Python.
- Consultas SQL parametrizadas.
- Operaciones CRUD.
- Manejo de excepciones.
- Validación de datos introducidos por el usuario.
- Variables de entorno.
- List comprehensions.
- Entornos virtuales y gestión de dependencias.
- Git y GitHub.

## Estado

Proyecto funcional desarrollado como parte de mi formación y práctica con Python y PostgreSQL.