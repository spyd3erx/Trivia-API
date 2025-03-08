from app import db

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text, nullable=False)
    correct_answer = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(15), nullable=False)

    scores = db.relationship('Score', back_populates='question')  # Relación uno a muchos

    def __str__(self):
        return f"(questions <id:{self.id}, question:{self.question_text}>)"