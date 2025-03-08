from app.models import Question, Score
from sqlalchemy.sql import func
import unicodedata
from app import db


def normalize_text(text):
    """Convierte el texto a minúsculas y elimina acentos"""
    if text is None:
        return None  # Si es None, retorna None directamente
    
    return ''.join(
        char for char in unicodedata.normalize('NFD', text.lower()) 
        if unicodedata.category(char) != 'Mn'
    )

def get_random_question():
    """This function returns a question based on the category and difficulty"""
    random_question = Question.query.order_by(func.random()).first()
    
    if random_question:
        # Convertir el objeto SQLAlchemy en un diccionario que coincida con el modelo
        return random_question
    else:
        return {'message': 'No hay preguntas disponibles'}, 404

def get_question_args(difficulty, category=None):
    """Esta función retorna una pregunta basada en la categoría y dificultad"""
    
    normalized_difficulty = normalize_text(difficulty)
    normalized_category = normalize_text(category) if category else None

    query = Question.query.filter(func.lower(Question.difficulty) == normalized_difficulty)

    if category:
        query = query.filter(func.lower(Question.category) == normalized_category)
        
    question = query.order_by(func.random()).first()

    return question

def validate_answer(question_id, user_answer, id_user):
    """This function validates the answer to a question(id)"""

    # Obtén la pregunta desde la base de datos basada en el ID
    check_answer = Question.query.get(question_id)
    if not check_answer:
        return None
    
    # Verifica si el usuario ya respondió correctamente esta pregunta
    existing_score = Score.query.filter_by(id_user=id_user, id_question=question_id, is_correct=True).first()
    if existing_score:
        return {
            "message": "You have already answered this question correctly.",
            "is_correct": True,
            "difficulty": check_answer.difficulty,
            "category": check_answer.category
        }, 400
    
    # Normaliza la respuesta del usuario y la respuesta correcta
    is_correct = normalize_text(check_answer.correct_answer) == normalize_text(user_answer)

    # Obtén o crea un registro de intentos para esta pregunta y usuario
    score = Score.query.filter_by(id_user=id_user, id_question=question_id).first()
    if not score:
        # Si no existe un registro, crea uno nuevo con 1 intento
        score = Score(id_user=id_user, id_question=question_id, attemps=1, is_correct=is_correct)
    else:
        # Si ya existe un registro, incrementa el número de intentos
        score.attemps += 1
        score.is_correct = is_correct  # Actualiza el campo is_correct

    # Guarda el registro en la base de datos
    db.session.add(score)
    db.session.commit()

    # Devuelve la respuesta
    return {
            "message": "Answer received",
            "is_correct": is_correct,
            "difficulty": check_answer.difficulty,
            "category": check_answer.category
        }, 200