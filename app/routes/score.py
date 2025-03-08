from flask_restx import Resource, Namespace, fields

api = Namespace('Score', description='Operations related to score')


score_model = api.model('Score', {
    'id_user': fields.Integer(description="ID del usuario"),
    'total_correct': fields.Integer(description="Total de respuestas correctas"),
    'total_attemps': fields.Integer(description="Total de intentos"),
})

@api.route('/')
class Score(Resource):
    @api.marshal_with(score_model)
    @api.doc(description='Just a test endpoint')
    def get(self):
        return {'score': 0}

@api.route('/<int:id_user>')
class Score(Resource):
    @api.marshal_with(score_model)
    @api.doc(description='Just a test endpoint')
    def get(self, id_user):
        return {'score': 0}