FROM python:3.10-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de requisitos e instalarlos
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . /app/

# Exponer el puerto que usa Render
EXPOSE 10000

# Comando para arrancar el servidor de Django de forma segura para Render
CMD ["python", "manage.py", "runserver", "0.0.0.0:10000"]
