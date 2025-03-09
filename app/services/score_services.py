from sqlalchemy import func, desc
from app.models import User, Score
from app import db

def show_all_score():
    # Consulta para obtener el nombre del usuario y el número de respuestas correctas
    query = db.session.query(
        User.username.label('user'),
        func.coalesce(func.count(Score.id), 0).label('correct_answers')  # Usa func.coalesce
    ).outerjoin(
        Score, (User.id == Score.id_user) & (Score.is_correct == 1)
    ).group_by(
        User.username
    ).order_by(
        desc('correct_answers')  # Ordena por correct_answers en orden descendente
    ).all()

    # Devuelve los resultados
    return query