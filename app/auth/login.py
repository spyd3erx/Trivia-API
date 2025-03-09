from flask import Blueprint, make_response, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.users_model import User
from app.ext import db


def register(username, password):

    user = User.query.filter_by(username = username).one_or_none()

    if user is not None:
        return jsonify(message='username exist')

    hashed_password = generate_password_hash(password)

    user = User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return user


def login(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=str(user.id)) # Create a token based on the user id, need to be a string
        response = {
            'message': 'Login successful',
            'access_token': access_token
        }
        return response, 200
    else:
        return {"message": "Login failed: Invalid username or password"}, 401