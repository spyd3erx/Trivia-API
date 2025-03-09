from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.users_services import show_profile

api = Namespace('User', description='Operations related to user')

score_model = api.model('ScoreId', {
    'attemps': fields.Integer(description="Total de intentos"),
    'id_question': fields.Integer(description="ID de la pregunta"),
    'solved_at': fields.DateTime(description="Fecha de resolución")
})

user_model = api.model('User', {
    'id': fields.Integer(description="ID del usuario"),
    'username': fields.String(description="Nombre de usuario"),
    'created_at': fields.DateTime(description="Fecha de creación del usuario"),
    'scores': fields.List(fields.Nested(score_model), description="Lista de puntuaciones del usuario")
})

@api.route('/')
class User(Resource):
    @jwt_required()
    @api.doc(security="jsonWebToken", description='Just a test endpoint')
    @api.marshal_with(user_model)
    def get(self):
        identity = get_jwt_identity()
        return show_profile(identity)