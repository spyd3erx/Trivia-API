from app import db
from datetime import datetime

class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id_question = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    total_correct = db.Column(db.Integer, nullable=False)
    total_attemps = db.Column(db.Integer, nullable=False)
    solved_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='scores')  # Relación muchos a uno
    question = db.relationship('Question', back_populates='scores')  # Relación muchos a uno

    def __str__(self):
        return f"(scores <id_user:{self.id_user}, total_correct:{self.total_correct}>)"