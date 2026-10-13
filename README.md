# Linux System Report

Herramienta desarrollada en Python para practicar la automatización de tareas de administración de sistemas Linux. El proyecto procesa información desde un archivo JSON y genera un registro con información del sistema.

## Funcionalidades

- Lectura de un archivo JSON proporcionado como argumento.
- Filtrado de registros según su estado (`completed`).
- Generación de un archivo de salida `logs_estado.txt`.
- Consulta de información del sistema mediante comandos como `df -h`, `uptime` y `ps`.
- Manejo de errores relacionados con argumentos, archivos y contenido JSON.
- Validación del tamaño del archivo de entrada.

## Tecnologías

- Python 3
- JSON
- Linux / WSL
- Comandos de administración del sistema
- Git y GitHub

## Requisitos

- Python 3 instalado.
- Linux o WSL para ejecutar los comandos del sistema.

## Uso

Ejecutá el script indicando la ruta del archivo JSON:

```bash
python3 system_report.py procesos.json
```

El archivo JSON debe contener los campos que espera el programa. Por ejemplo:

```json
[
  {
    "name": "tarea-ejemplo",
    "completed": false
  },
  {
    "name": "tarea-finalizada",
    "completed": true
  }
]
```

El programa procesa los registros según la lógica implementada y genera el archivo de salida correspondiente.

## Objetivo de aprendizaje

Este proyecto permite practicar el procesamiento de datos con Python, la lectura de archivos, el manejo de excepciones y la ejecución de comandos del sistema operativo.

## Estado del proyecto

Proyecto de práctica en evolución. La validación de entradas, el manejo de errores y la compatibilidad de los comandos con distintos entornos son aspectos que deben probarse y mejorarse de forma progresiva.

## Limitaciones

- La salida depende de los comandos disponibles en el sistema operativo.
- El formato del JSON debe ajustarse a lo esperado por el programa.
- El proyecto no reemplaza una herramienta profesional de monitorización o administración de sistemas.
