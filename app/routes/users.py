from flask_restx import Namespace, Resource, fields

api = Namespace('Users', description='Users related operations')


@api.route('/')
class User(Resource):
    @api.doc(description='Just a test endpoint')
    def get(self):
        return {'hello': 'world'}