from app.models.questions_models import Question
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
    return random_question

def get_question_args(difficulty, category=None):
    """Esta función retorna una pregunta basada en la categoría y dificultad"""
    
    normalized_difficulty = normalize_text(difficulty)
    normalized_category = normalize_text(category) if category else None

    query = Question.query.filter(func.lower(Question.difficulty) == normalized_difficulty)

    if category:
        query = query.filter(func.lower(Question.category) == normalized_category)
        
    question = query.order_by(func.random()).first()

    return question

def validate_answer(question_id, user_answer):
    """This function validates the answer to a question(id)"""

    #get the question from the database based on the id
    check_answer = Question.query.get(question_id)
    if not check_answer:
        return None

    #normalize the user answer and the correct answer
    is_correct = normalize_text(check_answer.correct_answer) == normalize_text(user_answer)

    return {
            "is_correct": is_correct,
            "correct_answer": check_answer.correct_answer,
            "difficulty": check_answer.difficulty,
            "category": check_answer.category
        }, 200 