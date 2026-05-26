from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from app.models import db, User, Question, Score, StudentAnswer
from datetime import datetime
import random

main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
quiz_bp = Blueprint('quiz', __name__, url_prefix='/quiz')


# ==================== MAIN ROUTES ====================
@main_bp.route('/')
def index():
    """Home page"""
    if 'user_id' in session:
        return redirect(url_for('main.dashboard'))
    return render_template('index.html')


@main_bp.route('/dashboard')
def dashboard():
    """Student dashboard with score history"""
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    user = User.query.get(session['user_id'])
    scores = Score.query.filter_by(user_id=session['user_id']).order_by(Score.quiz_date.desc()).all()
    
    return render_template('dashboard.html', user=user, scores=scores)


@main_bp.route('/help')
def help_page():
    """Help/guidance page for new users"""
    return render_template('help.html')


# ==================== AUTHENTICATION ROUTES ====================
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if not username or not email or not password:
            return render_template('register.html', error='All fields are required')
        
        if password != confirm_password:
            return render_template('register.html', error='Passwords do not match')
        
        if len(password) < 6:
            return render_template('register.html', error='Password must be at least 6 characters')
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            return render_template('register.html', error='Username already exists')
        
        if User.query.filter_by(email=email).first():
            return render_template('register.html', error='Email already exists')
        
        # Create new user
        user = User(username=username, email=email)
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('auth.login', success='Registration successful. Please login.'))
    
    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            return render_template('login.html', error='Username and password required')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('main.dashboard'))
        
        return render_template('login.html', error='Invalid username or password')
    
    success = request.args.get('success')
    return render_template('login.html', success=success)


@auth_bp.route('/logout')
def logout():
    """User logout"""
    session.clear()
    return redirect(url_for('main.index'))


# ==================== QUIZ ROUTES ====================
@quiz_bp.route('/start')
def start_quiz():
    """Start a new quiz"""
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    user = User.query.get(session['user_id'])
    return render_template('quiz_intro.html', user=user)


@quiz_bp.route('/quiz-interface')
def quiz_interface():
    """Quiz interface page"""
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    return render_template('quiz.html')


@quiz_bp.route('/get-questions')
def get_questions():
    """Get quiz questions (50 total: 25 Math + 25 Science)"""
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Get 25 random Math questions
    math_questions = Question.query.filter_by(subject='Math').order_by(db.func.random()).limit(25).all()
    
    # Get 25 random Science questions
    science_questions = Question.query.filter_by(subject='Science').order_by(db.func.random()).limit(25).all()
    
    # If not enough questions, fill with available ones
    if len(math_questions) < 25:
        math_questions = Question.query.filter_by(subject='Math').all()
    
    if len(science_questions) < 25:
        science_questions = Question.query.filter_by(subject='Science').all()
    
    # Combine questions
    all_questions = math_questions + science_questions
    
    # Format response
    questions_data = []
    for q in all_questions:
        questions_data.append({
            'id': q.id,
            'subject': q.subject,
            'question': q.question_text,
            'options': {
                'A': q.option_a,
                'B': q.option_b,
                'C': q.option_c,
                'D': q.option_d
            }
        })
    
    return jsonify({'questions': questions_data})


@quiz_bp.route('/submit', methods=['POST'])
def submit_quiz():
    """Submit quiz answers"""
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.get_json()
    answers = data.get('answers', {})
    time_spent = data.get('time_spent', 0)
    
    # Create score record
    score = Score(user_id=session['user_id'], time_spent=time_spent)
    db.session.add(score)
    db.session.flush()  # Get the score ID without committing
    
    math_score = 0
    science_score = 0
    
    # Process each answer
    for question_id, selected_option in answers.items():
        question = Question.query.get(int(question_id))
        if question:
            is_correct = selected_option == question.correct_option
            
            # Record answer
            student_answer = StudentAnswer(
                score_id=score.id,
                question_id=question.id,
                selected_option=selected_option,
                is_correct=is_correct
            )
            db.session.add(student_answer)
            
            # Update scores
            if is_correct:
                if question.subject == 'Math':
                    math_score += 1
                else:
                    science_score += 1
    
    # Update score record
    score.math_score = math_score
    score.science_score = science_score
    score.total_score = math_score + science_score
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'math_score': math_score,
        'science_score': science_score,
        'total_score': score.total_score,
        'score_id': score.id
    })


@quiz_bp.route('/results/<int:score_id>')
def results(score_id):
    """Display quiz results"""
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    score = Score.query.get_or_404(score_id)
    
    # Ensure the score belongs to the logged-in user
    if score.user_id != session['user_id']:
        return redirect(url_for('main.dashboard'))
    
    return render_template('results.html', score=score)
