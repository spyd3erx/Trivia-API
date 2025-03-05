from flask import Blueprint
from app.ext import api


api_bp = Blueprint('api_bp', __name__)
api.init_app(api_bp, title='Trivia API',version='0.1.0',
             description='Trivia API, play and fun :D')


from app.routes.questions import api as questions_ns
from app.routes.users import api as users_ns
from app.routes.score import api as score_ns

api.add_namespace(users_ns, path='/user')
api.add_namespace(questions_ns, path='/question')
api.add_namespace(score_ns, path='/score')