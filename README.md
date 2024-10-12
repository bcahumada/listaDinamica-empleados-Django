# Proyecto Django - Lista Dinámica de Empleados

Este proyecto es una aplicación web en Django que permite mostrar una lista dinámica de empleados. Los nombres de los empleados están almacenados en una lista en Python y se muestran de manera dinámica en una página web usando un template HTML. Además, el diseño de la página está estilizado con **Bootstrap**.

## Requisitos

Antes de comenzar, asegúrate de tener lo siguiente instalado:

- Python 3.x
- Django (versión más reciente)
- Bootstrap (incluido a través de CDN en el template HTML)

## Instalación

Pasos para configurar el proyecto:

1. Crear un entorno virtual.
```bash
python -m venv venv
```

2. Activa el entorno virtual:

Windows:
```bash
.\venv\Scripts\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

3. Instala Django en el entorno virtual:
```bash
pip install django
```
4. Crea un proyecto Django llamado institucion:
```bash
django-admin startproject institucion
```

5. Crea una aplicación dentro del proyecto llamada empleadosApp:
```bash
python manage.py startapp empleadosApp
```


6. Ejecuta las migraciones iniciales:
```bash
python manage.py migrate
```
7. Desarrollo del proyecto


## Ejecutar el Proyecto
Ejecuta el servidor de desarrollo:
```bash
python manage.py runserver
```

## Autor

Bárbara HA.