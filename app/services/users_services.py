from app import db
from app.models import User, Score

def show_profile(user_id):
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404

        # Obtener las puntuaciones del usuario
        scores = Score.query.filter_by(id_user=user_id).all()

        # Formatear la respuesta
        user_data = {
            'id': user.id,
            'username': user.username,
            'created_at': user.created_at.isoformat(),
            'scores': [
                {
                    'attemps': score.attemps,
                    'id_question': score.id_question,
                    'solved_at': score.solved_at.isoformat()
                }
                for score in scores
            ]
        }

        return user_data, 200