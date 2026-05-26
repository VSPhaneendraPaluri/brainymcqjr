// Quiz state management
let questions = [];
let currentQuestionIndex = 0;
let answers = {};
let timeRemaining = 3600; // 60 minutes in seconds
let timerInterval = null;
let timeStarted = Date.now();

// Initialize quiz
async function initQuiz() {
    try {
        const response = await fetch('/quiz/get-questions');
        if (!response.ok) {
            alert('Error loading questions. Please try again.');
            return;
        }
        
        const data = await response.json();
        questions = data.questions;
        
        document.getElementById('loading').style.display = 'none';
        document.getElementById('quiz-body').style.display = 'block';
        
        renderQuestionOverview();
        displayQuestion();
        startTimer();
    } catch (error) {
        console.error('Error:', error);
        alert('Error loading quiz. Please refresh the page.');
    }
}

// Display current question
function displayQuestion() {
    if (currentQuestionIndex >= questions.length) {
        return;
    }
    
    const question = questions[currentQuestionIndex];
    
    // Update question text
    document.getElementById('question-text').textContent = question.question;
    
    // Update options
    document.getElementById('option-a').textContent = question.options.A;
    document.getElementById('option-b').textContent = question.options.B;
    document.getElementById('option-c').textContent = question.options.C;
    document.getElementById('option-d').textContent = question.options.D;
    
    // Update subject badge
    document.getElementById('subject-badge').textContent = question.subject;
    
    // Reset radio buttons
    const radios = document.querySelectorAll('input[name="answer"]');
    radios.forEach(radio => radio.checked = false);
    
    // Check if answer was previously selected
    if (answers[question.id]) {
        const selectedRadio = document.querySelector(`input[name="answer"][value="${answers[question.id]}"]`);
        if (selectedRadio) {
            selectedRadio.checked = true;
        }
    }
    
    // Update question counter
    document.getElementById('question-counter').textContent = `Question ${currentQuestionIndex + 1} of ${questions.length}`;
    
    // Update progress bar
    const progress = ((currentQuestionIndex + 1) / questions.length) * 100;
    document.getElementById('progress-fill').style.width = `${progress}%`;
    
    // Update question overview
    updateQuestionOverview();
    
    // Update button states
    document.getElementById('prev-btn').disabled = currentQuestionIndex === 0;
    document.getElementById('next-btn').style.display = currentQuestionIndex === questions.length - 1 ? 'none' : 'block';
    document.getElementById('submit-btn').style.display = currentQuestionIndex === questions.length - 1 ? 'block' : 'none';
}

// Next question
function nextQuestion() {
    // Save answer
    const selectedAnswer = document.querySelector('input[name="answer"]:checked');
    if (selectedAnswer) {
        answers[questions[currentQuestionIndex].id] = selectedAnswer.value;
    }
    
    if (currentQuestionIndex < questions.length - 1) {
        currentQuestionIndex++;
        displayQuestion();
        document.querySelector('.quiz-sidebar').scrollTop = 0;
    }
}

// Previous question
function previousQuestion() {
    // Save answer
    const selectedAnswer = document.querySelector('input[name="answer"]:checked');
    if (selectedAnswer) {
        answers[questions[currentQuestionIndex].id] = selectedAnswer.value;
    }
    
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        displayQuestion();
        document.querySelector('.quiz-sidebar').scrollTop = 0;
    }
}

// Render question overview buttons
function renderQuestionOverview() {
    const container = document.getElementById('questions-overview');
    container.innerHTML = '';
    
    for (let i = 0; i < questions.length; i++) {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'question-btn';
        btn.textContent = i + 1;
        btn.onclick = () => goToQuestion(i);
        
        if (i === currentQuestionIndex) {
            btn.classList.add('current');
        }
        if (answers[questions[i].id]) {
            btn.classList.add('answered');
        }
        
        container.appendChild(btn);
    }
}

// Update question overview
function updateQuestionOverview() {
    const buttons = document.querySelectorAll('.question-btn');
    buttons.forEach((btn, index) => {
        btn.classList.remove('current', 'answered');
        if (index === currentQuestionIndex) {
            btn.classList.add('current');
        }
        if (answers[questions[index].id]) {
            btn.classList.add('answered');
        }
    });
}

// Go to specific question
function goToQuestion(index) {
    // Save current answer
    const selectedAnswer = document.querySelector('input[name="answer"]:checked');
    if (selectedAnswer) {
        answers[questions[currentQuestionIndex].id] = selectedAnswer.value;
    }
    
    currentQuestionIndex = index;
    displayQuestion();
    document.querySelector('.quiz-sidebar').scrollTop = 0;
}

// Start timer
function startTimer() {
    timerInterval = setInterval(() => {
        timeRemaining--;
        updateTimerDisplay();
        
        if (timeRemaining <= 0) {
            clearInterval(timerInterval);
            alert('Time is up! Submitting your quiz...');
            submitQuiz();
        }
    }, 1000);
}

// Update timer display
function updateTimerDisplay() {
    const minutes = Math.floor(timeRemaining / 60);
    const seconds = timeRemaining % 60;
    const timerElement = document.getElementById('timer');
    timerElement.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
    
    if (timeRemaining <= 300) {
        timerElement.classList.add('danger');
    } else if (timeRemaining <= 600) {
        timerElement.classList.add('warning');
    }
}

// Submit quiz
async function submitQuiz() {
    // Save last answer
    const selectedAnswer = document.querySelector('input[name="answer"]:checked');
    if (selectedAnswer) {
        answers[questions[currentQuestionIndex].id] = selectedAnswer.value;
    }
    
    // Calculate time spent
    const timeSpent = Math.floor((Date.now() - timeStarted) / 1000);
    
    // Clear timer
    clearInterval(timerInterval);
    
    // Show loading
    const quizContent = document.getElementById('quiz-body');
    const loading = document.createElement('div');
    loading.className = 'loading';
    loading.textContent = 'Submitting your quiz...';
    quizContent.appendChild(loading);
    
    try {
        const response = await fetch('/quiz/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                answers: answers,
                time_spent: timeSpent
            })
        });
        
        if (!response.ok) {
            alert('Error submitting quiz. Please try again.');
            location.reload();
            return;
        }
        
        const data = await response.json();
        
        // Redirect to results page
        window.location.href = `/quiz/results/${data.score_id}`;
    } catch (error) {
        console.error('Error:', error);
        alert('Error submitting quiz. Please try again.');
        location.reload();
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', initQuiz);
