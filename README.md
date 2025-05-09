# TRIVIA-API

## Descripción
Trivia-API es una API RESTful desarrollada con Flask y Flask-Restx que permite jugar juegos de trivia (preguntas y respuestas). Incluye funcionalidades de autenticación, manejo de usuarios, preguntas, puntuaciones.

## Características
- **Autenticación**: Registro y login de usuarios con JWT.
- **Gestión de usuarios**: Visualización del perfil de usuario y sus puntuaciones.
- **Preguntas**: Obtención de preguntas aleatorias o filtradas por dificultad y categoría.
- **Validación de respuestas**: Validación de respuestas a preguntas y registro de intentos.
- **Puntuaciones**: Visualización de las puntuaciones de los usuarios.
- **Swagger UI**: Documentación interactiva generada automáticamente con Flask-Restx.

## Requisitos
- Python 3.12 o superior
- [Poetry](https://python-poetry.org/) para la gestión de dependencias
- SQLite (base de datos por defecto)

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/trivia-api.git
   cd trivia-api
   ```

2. Instala las dependencias usando Poetry:
   ```bash
    poetry install
   ```

3. Crea un archivo *.env* en la raíz del proyecto y define las siguientes variables:
    ```bash
    SECRET_KEY=tu_clave_secreta
    JWT_SECRET_KEY=tu_clave_secreta_para_jwt
    DATABASE_URI=tu_string_de_coneccion
    ```
4. Realiza las migraciones de la base de datos:
    ```bash
        poetry run flask db upgrade
    ```

5. Inicia el servidor de desarrollo:
    ```bash
        poetry run python wsgi.py
    ```

## Docker

1. Construye la imagen:
    ```bash
    build -t trivia-api .
    ```

2. Ejecuta el contenedor:
    ```bash
    docker run -p 8000:8000 --env-file .env trivia-api
    ```
