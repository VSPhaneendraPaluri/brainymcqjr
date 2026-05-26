# BrainyMCQ Junior - Setup and Deployment Guide

## 📋 Project Overview

BrainyMCQ Junior is an interactive, open-source web platform designed for Class 3-5 students to test their knowledge in Mathematics and Science through multiple-choice questions.

### Key Features
- 🎓 50 MCQ questions per quiz (25 Math + 25 Science)
- 👤 Secure user authentication with encrypted passwords
- ⏱️ 60-minute timed quiz with real-time timer
- 📊 Comprehensive score history and progress tracking
- 📚 Subject-wise question organization
- 🎨 Responsive design for mobile, tablet, and desktop
- 🔒 Data isolation for each student
- 🌐 Deployable on local servers or cloud platforms

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7+** (Download from https://www.python.org/downloads/)
- **pip** (Python package manager, usually comes with Python)
- **Git** (Optional, for version control)
- **Web Browser** (Chrome, Firefox, Safari, or Edge)

---

## 💻 Local Installation & Setup

### Step 1: Clone or Navigate to the Project

```bash
# Navigate to the project directory
cd c:\phaneendra\codes\mcq-paper
```

### Step 2: Create a Virtual Environment

A virtual environment isolates project dependencies.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

Install all required packages from requirements.txt:

```bash
pip install -r requirements.txt
```

This will install:
- Flask 2.3.3 - Web framework
- Flask-SQLAlchemy 3.0.5 - Database ORM
- Werkzeug 2.3.7 - WSGI utilities for password hashing

### Step 4: Run the Application

```bash
python run.py
```

You should see output like:
```
╔═══════════════════════════════════════════════════════╗
║  BrainyMCQ Junior - Interactive Learning Platform    ║
║  Class 3-5 Mathematics & Science Quiz                ║
╚═══════════════════════════════════════════════════════╝

🚀 Starting BrainyMCQ Junior...
📚 Navigate to: http://localhost:5000
```

### Step 5: Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

---

## 👤 First-Time User Guide

### 1. Register Your Account

1. Click on **"Register"** button on the homepage
2. Enter a **username** (e.g., "student_001")
3. Enter your **email** (e.g., "student@example.com")
4. Create a **strong password** (minimum 6 characters)
5. Click **"Register"** button
6. You'll be redirected to the login page

### 2. Login to Your Account

1. Enter your **username**
2. Enter your **password**
3. Click **"Login"** button
4. You'll be directed to your personal dashboard

### 3. Start a Quiz

1. From your **Dashboard**, click **"Start New Quiz"**
2. Review the quiz guidelines
3. Click **"Begin Quiz"** to start
4. Answer all 50 questions (25 Math + 25 Science)
5. Use **Previous/Next** buttons to navigate
6. Click **"Submit Quiz"** when done

### 4. View Results

- Your score will be displayed immediately
- See subject-wise breakdown (Math & Science)
- View time taken and percentage scored
- Get personalized feedback based on performance

### 5. Track Progress

- Visit your **Dashboard** anytime
- View complete history of all quiz attempts
- See scores and timestamps for each attempt

---

## 📁 Project Structure

```
mcq-paper/
├── run.py                      # Main application entry point
├── requirements.txt            # Python dependencies
├── instructions.md             # Original project requirements
├── README.md                   # This file
│
├── app/
│   ├── __init__.py            # Application factory
│   ├── models.py              # Database models (User, Question, Score, etc.)
│   ├── routes.py              # Flask routes/blueprints
│   ├── seed_questions.py      # Question database seeding
│   │
│   ├── templates/
│   │   ├── base.html          # Base template with layout
│   │   ├── index.html         # Homepage
│   │   ├── login.html         # Login page
│   │   ├── register.html      # Registration page
│   │   ├── dashboard.html     # Student dashboard
│   │   ├── quiz_intro.html    # Quiz introduction
│   │   ├── quiz.html          # Quiz interface
│   │   ├── results.html       # Results display
│   │   └── help.html          # Help/getting started
│   │
│   └── static/
│       ├── css/
│       │   └── style.css      # Main stylesheet
│       └── js/
│           ├── main.js        # General utilities
│           └── quiz.js        # Quiz functionality
│
└── mcq_quiz.db                # SQLite database (created on first run)
```

---

## 🗄️ Database Structure

### Tables

1. **Users**
   - Stores student credentials and profiles
   - Passwords are securely hashed

2. **Questions**
   - Contains all 50 MCQ questions (25 Math + 25 Science)
   - Fields: subject, question_text, options (A-D), correct_option

3. **Scores**
   - Records quiz attempts with scores
   - Fields: user_id, math_score, science_score, total_score, time_spent

4. **StudentAnswers**
   - Tracks individual student responses
   - Fields: score_id, question_id, selected_option, is_correct

---

## 🔐 Security Features

- ✅ Password hashing using Werkzeug
- ✅ Session management for user authentication
- ✅ Data isolation between students
- ✅ CSRF protection (can be enhanced in production)
- ✅ Input validation on all forms

---

## 📤 Deployment on Free Indian Servers

### Option 1: Render (Free Tier)

1. Create account at https://render.com
2. Push code to GitHub
3. Connect repository to Render
4. Set environment variables
5. Deploy

### Option 2: Railway.app

1. Create account at https://railway.app
2. Connect GitHub repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python run.py`
5. Deploy

### Option 3: PythonAnywhere

1. Create account at https://www.pythonanywhere.com
2. Upload files via SFTP or Git
3. Configure virtual environment
4. Set up web app through dashboard
5. Deploy

### Option 4: Heroku (Free tier deprecated, but can use with paid options)

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution:** Ensure virtual environment is activated and requirements installed
```bash
pip install -r requirements.txt
```

### Issue: "Port 5000 already in use"
**Solution:** Use different port
```bash
python run.py
# Modify run.py: app.run(port=5001)
```

### Issue: Database locked or corrupted
**Solution:** Delete mcq_quiz.db and restart
```bash
rm mcq_quiz.db  # On Linux/Mac
del mcq_quiz.db  # On Windows
python run.py   # Restart
```

### Issue: Questions not loading
**Solution:** Check that seed_questions.py ran successfully
```python
# Manually run in Python shell:
from app import create_app
from app.seed_questions import seed_database
app = create_app()
seed_database(app)
```

---

## 📊 Admin Commands

### Access Database via Python Shell

```python
from app import create_app
from app.models import db, User, Question, Score

app = create_app()

# List all users
with app.app_context():
    users = User.query.all()
    for user in users:
        print(f"Username: {user.username}, Email: {user.email}")
    
    # View scores
    scores = Score.query.all()
    for score in scores:
        print(f"User: {score.user.username}, Score: {score.total_score}/50")
```

---

## 🚀 Performance Optimization

- Database queries are optimized
- Questions are randomly selected (reduce cheating)
- Static files are cached in browser
- Session management is efficient

---

## 📝 Adding More Questions

Edit `app/seed_questions.py`:

```python
NEW_MATH_QUESTIONS = [
    {
        'question': 'Your question here?',
        'options': {'A': 'Option A', 'B': 'Option B', 'C': 'Option C', 'D': 'Option D'},
        'correct': 'B'
    },
    # ... more questions
]
```

Then run:
```bash
python run.py  # Restart to seed new questions
```

---

## 📞 Support & Feedback

For bugs, feature requests, or support:
1. Check the Help section in the application (http://localhost:5000/help)
2. Review the code comments
3. Check Flask documentation: https://flask.palletsprojects.com/

---

## 📜 Technology Stack

### Backend
- **Flask**: Lightweight Python web framework
- **SQLAlchemy**: Database ORM
- **SQLite**: Default database (upgradeable to PostgreSQL)

### Frontend
- **HTML5**: Markup language
- **CSS3**: Styling with responsive design
- **JavaScript**: Quiz logic and interactivity
- **Bootstrap-inspired**: Custom responsive grid

### Server
- **Python WSGI**: Application server
- **Werkzeug**: Security utilities

---

## 🎯 Future Enhancements

Potential features for future versions:
- [ ] Mobile app (React Native/Flutter)
- [ ] Real-time leaderboards
- [ ] Difficulty levels (Easy/Medium/Hard)
- [ ] Category-wise topics
- [ ] Video explanations
- [ ] Performance analytics
- [ ] Admin dashboard
- [ ] Email notifications
- [ ] Two-factor authentication
- [ ] Question bank management system

---

## 📄 License

This project is open-source and free to use for educational purposes.

---

## ✅ Verification Checklist

- [x] 50 MCQ questions (25 Math + 25 Science)
- [x] User registration and login
- [x] Secure password storage
- [x] 60-minute timed quiz
- [x] Subject-wise question display
- [x] Score history tracking
- [x] Database schema for data isolation
- [x] Responsive design
- [x] Help/guidance for new users
- [x] Local deployment ready
- [x] Deployable to cloud platforms
- [x] requirements.txt with all dependencies

---

**Thank you for using MCQ Quiz Master! Happy Learning! 🎓**

For getting started, visit: http://localhost:5000/help
