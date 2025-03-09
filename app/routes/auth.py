from flask_restx import Namespace, Resource, fields
from app.auth.login import register, login
from app.api import authorizations

api = Namespace('auth',
        authorizations=authorizations,
        security='jsonWebToken', description='auth operations')

auth_model = api.model('Auth', {
    'username': fields.String(required=True, description='username'),
    'password': fields.String(required=True, description='password')
})

auth_register_model = api.model('AuthRegister', {
    'id': fields.Integer(description='id'),
    'username': fields.String(required=True, description='username')
})

auth_login_model = api.model('AuthLogin', {
    'message': fields.String(description='message'),
    'access_token': fields.String(description='access_token')
})


@api.route('/register')    
class Register(Resource):
    @api.expect(auth_model)
    @api.marshal_with(auth_register_model)
    @api.doc(description='register')
    def post(self):
        data = api.payload
        user, password = data['username'], data['password']
        return register(user, password)

@api.route('/login')
class Login(Resource):
    @api.expect(auth_model)
    @api.marshal_with(auth_login_model)
    @api.doc(description='login')
    def post(self):
        data = api.payload
        user, password = data['username'], data['password']
        return login(user, password)


