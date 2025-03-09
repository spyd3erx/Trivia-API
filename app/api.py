from app.ext import api


authorizations = {
    'jsonWebToken': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'Ingresa el token JWT en el formato: Bearer <token>'
    }
}

def create_swagger(app):

    # Inicializar api con authorizations y security
    api.init_app(
        app=app,
        version='1.0',
        title='API de Trivia',
        description='API para el juego de trivia'
    )

    # Importar namespaces
    from app.routes.questions import api as questions_ns
    from app.routes.score import api as score_ns
    from app.routes.auth import api as auth_ns
    from app.routes.user import api as user_ns

    # Registrar namespaces con el prefijo /api/v1
    api.add_namespace(auth_ns, path='/api/v1/auth')
    api.add_namespace(user_ns, path='/api/v1/user')
    api.add_namespace(questions_ns, path='/api/v1/question')
    api.add_namespace(score_ns, path='/api/v1/score')