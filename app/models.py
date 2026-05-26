from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    """User model for storing student credentials"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    # Relationship to scores
    scores = db.relationship('Score', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        """Hash and set password"""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if provided password matches hash"""
        return check_password_hash(self.password, password)


class Question(db.Model):
    """Question model for storing MCQ questions"""
    __tablename__ = 'questions'
    
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(20), nullable=False)  # 'Math' or 'Science'
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(255), nullable=False)
    option_b = db.Column(db.String(255), nullable=False)
    option_c = db.Column(db.String(255), nullable=False)
    option_d = db.Column(db.String(255), nullable=False)
    correct_option = db.Column(db.String(1), nullable=False)  # 'A', 'B', 'C', or 'D'
    difficulty_level = db.Column(db.String(20), default='Medium')  # Easy, Medium, Hard
    
    # Relationship to student answers
    answers = db.relationship('StudentAnswer', backref='question', lazy=True, cascade='all, delete-orphan')


class Score(db.Model):
    """Score model for storing student quiz results"""
    __tablename__ = 'scores'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quiz_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    math_score = db.Column(db.Integer, default=0)
    science_score = db.Column(db.Integer, default=0)
    total_score = db.Column(db.Integer, default=0)
    time_spent = db.Column(db.Integer)  # in seconds
    
    # Relationship to student answers
    answers = db.relationship('StudentAnswer', backref='score', lazy=True, cascade='all, delete-orphan')


class StudentAnswer(db.Model):
    """StudentAnswer model to track individual question responses"""
    __tablename__ = 'student_answers'
    
    id = db.Column(db.Integer, primary_key=True)
    score_id = db.Column(db.Integer, db.ForeignKey('scores.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    selected_option = db.Column(db.String(1), nullable=False)
    is_correct = db.Column(db.Boolean, default=False)
