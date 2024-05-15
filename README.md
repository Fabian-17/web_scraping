# Web Scraping con Python

Este script en Python te permite realizar web scraping en la página de Wikipedia para obtener información sobre Python y guardar los datos en un archivo JSON.

## Requisitos 
- Python 3.x: Si no lo tienes instalado, puedes descargarlo desde [python.org](https://www.python.org/downloads/).
- pip: El gestor de paquetes de Python. Generalmente se instala automáticamente con Python 3.

## Configuración del Entorno Virtual

Se recomienda usar entornos virtuales para evitar conflictos entre las dependencias de diferentes proyectos. Sigue estos pasos para crear y activar un entorno virtual:

```bash
# Instalar la herramienta virtualenv si no está instalada
pip install virtualenv

# Crear un nuevo entorno virtual
virtualenv venv

# Activar el entorno virtual (Windows)
venv\Scripts\activate
# o (Linux/macOS)
source venv/bin/activate
```

## Instalación de Dependencias
Para instalar las librerías necesarias, ejecuta el siguiente comando después de activar tu entorno virtual:

```bash
pip install requests
```

```bash
pip install BeautifulSoup4
```

## Uso

Una vez instaladas las dependencias, puedes ejecutar el script para obtener los datos de la página de Wikipedia sobre Python.
```bash
python app.py
```

Esto generará un archivo JSON en el directorio results llamado results.json que contiene los datos recopilados.