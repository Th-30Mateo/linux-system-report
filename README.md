# Linux System Report

Python automation script for Linux that processes information from a JSON file and generates a system report in `.txt` format.

## Features

* Reads a JSON file provided as a command-line argument.
* Identifies incomplete processes from the JSON data.
* Generates a system report in `logs_estado.txt`.
* Collects Linux system information using:

  * `df -h`
  * `uptime`
  * `ps`
* Handles common errors such as:

  * Missing command-line arguments.
  * File not found.
  * Invalid JSON format.
* Controls the output file size and deletes it when it reaches 10 MB.

## Technologies

* Python 3
* JSON
* Linux / WSL
* `subprocess`
* `sys`
* `os`
* `datetime`

## Usage

Run the script from a Linux environment or WSL:

```bash
python3 system_report.py procesos.json
```

The script generates:

```text
logs_estado.txt
```

## Example

The generated report contains information such as:

```text
====REPORTE DE ERROR====

Fecha: 18-09-2026 03:22:15

Procesos incompletos:
- Backup del sistema
- Verificación de disco

====EVALUACIÓN DEL SISTEMA====

Filesystem      Size  Used Avail Use%
...
```

## Environment

This project was developed and tested in a Linux environment using WSL.

## Objective

The main objective of this project is to practice Python automation applied to Linux system administration, including file handling, JSON processing, command execution, error handling, and system information collection.
