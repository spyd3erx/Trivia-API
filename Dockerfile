# Usar la imagen oficial de Python 3.12 slim
FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de dependencias
COPY poetry.lock pyproject.toml ./

# Instalar Poetry y Gunicorn
RUN pip install --upgrade pip && \
    pip install poetry

# Configurar Poetry para no crear un entorno virtual
RUN poetry config virtualenvs.create false

RUN poetry install --no-root

RUN poetry add gunicorn

# Copiar el resto del proyecto
COPY . .

# Exponer el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación con Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:create_app()"]
