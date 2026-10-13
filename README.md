# Linux System Report

Script de Python para practicar la automatización de tareas de administración de sistemas Linux. Procesa un archivo JSON con registros de procesos o tareas y genera un reporte de texto con los elementos incompletos y cierta información del sistema.

## Funcionalidades

- Lee un archivo JSON indicado como argumento de línea de comandos.
- Valida que el contenido sea una lista de objetos con las claves obligatorias `title`, `id` y `completed`.
- Comprueba que `completed` sea un valor booleano.
- Filtra los registros cuyo estado sea `completed: false`.
- Genera o amplía el archivo `logs_estado.txt`.
- Incluye fecha y hora del reporte.
- Recopila información del sistema mediante `df -h`, `uptime` y `ps aux --sort=-%mem`.
- Limita el tamaño del archivo de entrada previsto por el programa a 10 MiB.

## Tecnologías

- Python 3
- JSON
- Linux / WSL
- Módulos estándar: `json`, `sys`, `datetime`, `os` y `subprocess`

## Requisitos

- Python 3.
- Un entorno Linux o WSL con los comandos `df`, `uptime` y `ps` disponibles.

## Instalación

Cloná el repositorio:

```bash
git clone https://github.com/Th-30Mateo/linux-system-report.git
cd linux-system-report
```

No requiere instalar dependencias externas de Python: utiliza módulos de la biblioteca estándar.

## Formato del archivo JSON

El archivo debe contener una lista de objetos. Cada objeto debe incluir `title`, `id` y `completed`.

Ejemplo válido (`procesos.json`):

```json
[
  {
    "title": "Actualizar paquetes",
    "id": 101,
    "completed": false
  },
  {
    "title": "Revisar espacio en disco",
    "id": 102,
    "completed": true
  },
  {
    "title": "Verificar servicios",
    "id": 103,
    "completed": false
  }
]
```

En este ejemplo, el reporte incluirá los registros 101 y 103, porque tienen `completed: false`.

## Ejecución

Desde el directorio del proyecto, ejecutá:

```bash
python3 system_report.py procesos.json
```

Si el archivo se encuentra en otra ubicación, indicá su ruta.

## Resultado

El programa crea o amplía el archivo `logs_estado.txt` en el directorio desde el que se ejecuta.

El reporte incluye:

- Fecha y hora de generación.
- Título e identificador de cada registro incompleto.
- Información del espacio en disco.
- Tiempo de actividad del sistema.
- Una selección de las primeras líneas de la salida de `ps`, ordenadas por uso de memoria.

En la terminal se informa si el JSON se leyó correctamente, cuántos registros incompletos se encontraron y si se generó el reporte.

## Manejo de errores

El script contempla situaciones como:

- No proporcionar el argumento del archivo.
- No encontrar el archivo indicado.
- Encontrar un JSON inválido.
- Recibir una estructura que no sea una lista de objetos.
- Detectar claves obligatorias ausentes o un valor no booleano en `completed`.
- No poder abrir el archivo de salida por falta de permisos.

## Limitaciones conocidas

- El programa valida la presencia de las claves obligatorias, pero no comprueba todos sus tipos de datos.
- El archivo `logs_estado.txt` se amplía en cada ejecución; solo se elimina cuando ya existe y su tamaño es igual o superior a 10 MiB al comenzar.
- La información del sistema depende de los comandos disponibles en el entorno.
- El programa no es una herramienta integral de monitorización ni sustituye soluciones profesionales.

## Objetivo de aprendizaje

Practicar lectura y validación de JSON, manejo de archivos, excepciones, argumentos de consola y ejecución de comandos del sistema operativo desde Python.

## Estado

Proyecto de práctica en evolución.
