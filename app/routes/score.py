from flask_restx import Resource, Namespace, fields
from app.services.score_services import show_all_score

api = Namespace('Score', description='Operations related to score')


score_model = api.model('Score', {
    'user': fields.String(description="usuario"),
    'correct_answers': fields.Integer(description="Total de respuestas correctas"),
})


@api.route('/')
class Score(Resource):
    @api.marshal_with(score_model)
    @api.doc(description='Just a test endpoint')
    def get(self):
        return show_all_score()
