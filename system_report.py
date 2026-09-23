
#!/usr/bin/env python3

import sys
import json
import datetime
import os
import subprocess

# Creamos la variable "valid_param" que aloja el archivo json a analizar
# Se debe ingresar en consola despues de la ejecucion
try:
    valid_param = sys.argv[1]
except IndexError:
    print("ERROR: debes proporcionar como argumento un archivo JSON")
    sys.exit(1)

out_file = "logs_estado.txt"
limit_size = 10 * 1024 * 1024

# Creamos una validacion para corroborar que existe y no supera el limite de espacio

if os.path.exists(out_file):
        if os.path.getsize(out_file) >= limit_size:
                # En caso que supere el limite de 10MB se elimina.
                os.remove(out_file)

try:
    with open(valid_param, mode="r", encoding="utf-8") as file:
        logs = json.load(file)
        required_keys = {"title", "id", "completed"}

        if not isinstance(logs, list):
            print("ERROR: el json debe contener una lista")
            sys.exit(1)

        for process in logs:
            
            if not isinstance(process, dict):
                print("ERROR: cada proceso debe ser un objeto (dict)") 
                sys.exit(1)

            if not required_keys.issubset(process):
                print("ERROR: faltan claves obligatorias")
                sys.exit(1)

            if not isinstance(process['completed'], bool):
                print("ERROR: 'completed' debe ser un valor boolean")
                sys.exit(1)

        data = [process for process in logs if not process["completed"]]
        print("JSON abierto correctamente.")
        # Abrimos el archivo que recibimos como parametro
    

except FileNotFoundError:
    print("No se encontró el archivo .json")
    sys.exit(1)

except json.JSONDecodeError:
     print("ERROR el archivo no contiene un JSON valido")
     sys.exit(1)

try:
    with open(out_file, mode="a", encoding="utf-8") as dat:
        # Generamos un timestamp (sello de tiempo) al momento de creacion

        date_report = datetime.datetime.now().strftime("%d-%m-%Y")
        time_report = datetime.datetime.now().strftime("%H:%M:%S")
        dat.write(f"\n====REPORTE DE ERROR====\n")
        dat.write(f"\nFECHA: {date_report}\nHORA: {time_report}\n")

        # Escribimos el archivo .txt con los datos del log y el ID de proceso

        for i in data:
                line = f"\nPROCESO: {i['title']}\nID: {i['id']}\n"
                dat.write(line)
        eq = "="*30

        dat.write(f"\n{eq}\nEvaluacion del sistema\n{eq}\n")

        # Añadimos estado general de la maquina utilizando la libreria subprocess
        # Y añadimos los resultados de los comandos al .txt
        try:
            disk_space = subprocess.run(
                ["df","-h"],
                capture_output=True,
                text=True,
                check=True
                )
        except subprocess.CalledProcessError:
             print("ERROR: no se pudo ejecutar el comando 'df -h'")
             sys.exit(1)
        try:
            time_on_cpu = subprocess.run(
                ["uptime"],
                capture_output=True,
                text=True,
                check=True
                )
        except subprocess.CalledProcessError:
             print("ERROR: no se pudo ejecutar el comando 'uptime'")
             sys.exit(1)
        try:
            ps_result = subprocess.run(
                ["ps", "aux", "--sort=-%mem"],
                capture_output=True,
                text=True,
                check=True
                )
            use_cpu_mem = "\n".join(ps_result.stdout.splitlines()[:6])
        except subprocess.CalledProcessError:
             print("ERROR: el comando 'ps' no se pudo ejecutar")
             sys.exit(1)
        dat.write(f"\n\nEspacio en disco:\n\n{disk_space.stdout}\n{eq}\n")
        dat.write(f"\nTiempo de encendido del sistema:\n\n{time_on_cpu.stdout}\n{eq}\n" )
        dat.write(f"\nUso de RAM y CPU:\n\n{use_cpu_mem.stdout}\n{eq}\n")
        print(eq)
        print("✓ Archivo JSON leído correctamente.")
        print(f"✓ {len(data)} procesos incompletos encontrados.")
        print(f"✓ Reporte generado correctamente: {out_file}")
        print(eq)
except PermissionError:
     print("ERROR, no tienes autorizacion para abrir el archivo de salida")
