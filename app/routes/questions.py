from flask_restx import Resource, Namespace, fields, reqparse
from app.services.questions_services import get_random_question, get_question_args, validate_answer

#crear namespace para los endpoints de preguntas
api = Namespace('Questions', description='Operations related to questions')

# Definir los parámetros de la query con reqparse
query_parser = reqparse.RequestParser()
query_parser.add_argument('category', type=str, required=False, help='Category of the question')
query_parser.add_argument('difficulty', type=str, required=True, help='Difficulty of the question')


answer_model = api.model('Answer', {
    'question_id': fields.Integer(description="ID de la pregunta"),
    'user_answer': fields.String(description="Respuesta a la pregunta")
})

# Definir los modelos de pregunta con fields
question_summary_model = api.model('QuestionSummary', {
    'id': fields.Integer(description="ID de la pregunta"),
    'question_text': fields.String(description="Texto de la pregunta")
})

# Definir el modelo de respuesta de la pregunta con fields
question_answer_model = api.model('QuestionAnswer', {
    'is_correct': fields.Boolean(description="Indica si la respuesta es correcta"),
    'correct_answer': fields.String(description="Respuesta correcta"),
    'difficulty': fields.String(description="Dificultad de la pregunta"),
    'category': fields.String(description="Categoría de la pregunta")
})


@api.route('/')
class Question(Resource):

    @api.expect(query_parser) #indica que el endpoint espera datos de entrada(parametros de la query)
    @api.marshal_with(question_summary_model)
    @api.doc(description="Obtener una pregunta en función de la categoría(opcional) y la dificultad(requerida)")
    def get(self):
        args = query_parser.parse_args()
        category = args.get('category')
        difficulty = args.get('difficulty')

        return get_question_args(difficulty, category)

@api.route('/random')
class QuestionRandom(Resource):

    @api.marshal_with(question_summary_model)
    @api.doc(description="Obtener una pregunta aleatoria")
    def get(self):
        return get_random_question()
    
@api.route('/answer')
class Answer(Resource):

    @api.expect(answer_model)
    @api.marshal_with(question_answer_model)
    @api.doc(description="Enviar la respuesta a una pregunta")
    def post(self):
        answer = api.payload #recibe los datos de entrada
        question_id = answer.get("question_id")
        user_answer = answer.get("user_answer")
        return  validate_answer(question_id, user_answer)