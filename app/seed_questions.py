"""
Script to seed the database with sample MCQ questions for Class 3-5 students
"""
from app.models import db, Question

# Mathematics Questions (Class 3-5 Level)
MATH_QUESTIONS = [
    {
        'question': 'What is 15 + 8?',
        'options': {'A': '22', 'B': '23', 'C': '24', 'D': '25'},
        'correct': 'B'
    },
    {
        'question': 'What is 50 - 23?',
        'options': {'A': '25', 'B': '26', 'C': '27', 'D': '28'},
        'correct': 'C'
    },
    {
        'question': 'What is 12 × 5?',
        'options': {'A': '55', 'B': '60', 'C': '65', 'D': '70'},
        'correct': 'B'
    },
    {
        'question': 'What is 144 ÷ 12?',
        'options': {'A': '10', 'B': '11', 'C': '12', 'D': '13'},
        'correct': 'C'
    },
    {
        'question': 'Which is the largest number: 456, 465, 564, 546?',
        'options': {'A': '456', 'B': '465', 'C': '564', 'D': '546'},
        'correct': 'C'
    },
    {
        'question': 'What is 1/2 + 1/4?',
        'options': {'A': '1/6', 'B': '3/4', 'C': '1/2', 'D': '2/3'},
        'correct': 'B'
    },
    {
        'question': 'How many sides does a pentagon have?',
        'options': {'A': '4', 'B': '5', 'C': '6', 'D': '7'},
        'correct': 'B'
    },
    {
        'question': 'What is 25% of 200?',
        'options': {'A': '25', 'B': '40', 'C': '50', 'D': '75'},
        'correct': 'C'
    },
    {
        'question': 'Which number comes next: 2, 4, 6, 8, ?',
        'options': {'A': '9', 'B': '10', 'C': '11', 'D': '12'},
        'correct': 'B'
    },
    {
        'question': 'What is the area of a square with side 5 cm?',
        'options': {'A': '10 cm²', 'B': '20 cm²', 'C': '25 cm²', 'D': '30 cm²'},
        'correct': 'C'
    },
    {
        'question': 'What is 9²?',
        'options': {'A': '81', 'B': '72', 'C': '63', 'D': '54'},
        'correct': 'A'
    },
    {
        'question': 'What is the perimeter of a rectangle with length 6 cm and width 4 cm?',
        'options': {'A': '10 cm', 'B': '12 cm', 'C': '20 cm', 'D': '24 cm'},
        'correct': 'C'
    },
    {
        'question': 'What is 3/4 of 80?',
        'options': {'A': '50', 'B': '60', 'C': '70', 'D': '80'},
        'correct': 'B'
    },
    {
        'question': 'What is the sum of angles in a triangle?',
        'options': {'A': '90°', 'B': '180°', 'C': '270°', 'D': '360°'},
        'correct': 'B'
    },
    {
        'question': 'What is 7 × 8?',
        'options': {'A': '54', 'B': '55', 'C': '56', 'D': '57'},
        'correct': 'C'
    },
    {
        'question': 'Which is a prime number: 9, 12, 17, 21?',
        'options': {'A': '9', 'B': '12', 'C': '17', 'D': '21'},
        'correct': 'C'
    },
    {
        'question': 'What is 48 ÷ 6?',
        'options': {'A': '6', 'B': '7', 'C': '8', 'D': '9'},
        'correct': 'C'
    },
    {
        'question': 'What is 100 - 35?',
        'options': {'A': '60', 'B': '65', 'C': '70', 'D': '75'},
        'correct': 'B'
    },
    {
        'question': 'How many minutes are in 2 hours?',
        'options': {'A': '60', 'B': '90', 'C': '120', 'D': '150'},
        'correct': 'C'
    },
    {
        'question': 'What is the value of π (approximately)?',
        'options': {'A': '2.14', 'B': '3.14', 'C': '4.14', 'D': '5.14'},
        'correct': 'B'
    },
    {
        'question': 'What is 250 + 150?',
        'options': {'A': '300', 'B': '350', 'C': '400', 'D': '450'},
        'correct': 'C'
    },
    {
        'question': 'What is the median of 2, 4, 6, 8, 10?',
        'options': {'A': '4', 'B': '6', 'C': '8', 'D': '10'},
        'correct': 'B'
    },
    {
        'question': 'How many sides does a hexagon have?',
        'options': {'A': '5', 'B': '6', 'C': '7', 'D': '8'},
        'correct': 'B'
    },
    {
        'question': 'What is 5³?',
        'options': {'A': '100', 'B': '110', 'C': '125', 'D': '150'},
        'correct': 'C'
    },
    {
        'question': 'What is 30% of 300?',
        'options': {'A': '60', 'B': '70', 'C': '80', 'D': '90'},
        'correct': 'D'
    },
]

# Science Questions (Class 3-5 Level)
SCIENCE_QUESTIONS = [
    {
        'question': 'What is the main source of energy for Earth?',
        'options': {'A': 'Moon', 'B': 'Sun', 'C': 'Wind', 'D': 'Water'},
        'correct': 'B'
    },
    {
        'question': 'How many planets are there in our solar system?',
        'options': {'A': '7', 'B': '8', 'C': '9', 'D': '10'},
        'correct': 'B'
    },
    {
        'question': 'Which gas do plants absorb from the atmosphere?',
        'options': {'A': 'Oxygen', 'B': 'Nitrogen', 'C': 'Carbon Dioxide', 'D': 'Hydrogen'},
        'correct': 'C'
    },
    {
        'question': 'What is the process by which plants make their own food?',
        'options': {'A': 'Respiration', 'B': 'Digestion', 'C': 'Photosynthesis', 'D': 'Fermentation'},
        'correct': 'C'
    },
    {
        'question': 'Which organ in the human body pumps blood?',
        'options': {'A': 'Lungs', 'B': 'Heart', 'C': 'Brain', 'D': 'Liver'},
        'correct': 'B'
    },
    {
        'question': 'How many bones are in the adult human skeleton?',
        'options': {'A': '186', 'B': '206', 'C': '226', 'D': '246'},
        'correct': 'B'
    },
    {
        'question': 'What is the freezing point of water in Celsius?',
        'options': {'A': '-10°C', 'B': '0°C', 'C': '10°C', 'D': '20°C'},
        'correct': 'B'
    },
    {
        'question': 'What is the boiling point of water in Celsius?',
        'options': {'A': '50°C', 'B': '75°C', 'C': '100°C', 'D': '125°C'},
        'correct': 'C'
    },
    {
        'question': 'Which is the smallest unit of life?',
        'options': {'A': 'Atom', 'B': 'Cell', 'C': 'Molecule', 'D': 'Organ'},
        'correct': 'B'
    },
    {
        'question': 'What do we call the process by which water changes into vapor?',
        'options': {'A': 'Condensation', 'B': 'Evaporation', 'C': 'Freezing', 'D': 'Melting'},
        'correct': 'B'
    },
    {
        'question': 'How many continents are there?',
        'options': {'A': '5', 'B': '6', 'C': '7', 'D': '8'},
        'correct': 'C'
    },
    {
        'question': 'Which metal is liquid at room temperature?',
        'options': {'A': 'Iron', 'B': 'Silver', 'C': 'Mercury', 'D': 'Gold'},
        'correct': 'C'
    },
    {
        'question': 'What is the speed of light approximately?',
        'options': {'A': '100,000 km/s', 'B': '200,000 km/s', 'C': '300,000 km/s', 'D': '400,000 km/s'},
        'correct': 'C'
    },
    {
        'question': 'Which vitamin is produced by exposure to sunlight?',
        'options': {'A': 'Vitamin A', 'B': 'Vitamin C', 'C': 'Vitamin D', 'D': 'Vitamin E'},
        'correct': 'C'
    },
    {
        'question': 'What is the largest organ in the human body?',
        'options': {'A': 'Brain', 'B': 'Heart', 'C': 'Skin', 'D': 'Lungs'},
        'correct': 'C'
    },
    {
        'question': 'Which of these is NOT a renewable energy source?',
        'options': {'A': 'Solar', 'B': 'Wind', 'C': 'Coal', 'D': 'Hydroelectric'},
        'correct': 'C'
    },
    {
        'question': 'What are the three states of matter?',
        'options': {'A': 'Solid, Liquid, Gas', 'B': 'Hard, Soft, Medium', 'C': 'Hot, Cold, Warm', 'D': 'Large, Small, Tiny'},
        'correct': 'A'
    },
    {
        'question': 'Which element has the chemical symbol "O"?',
        'options': {'A': 'Gold', 'B': 'Oxygen', 'C': 'Iron', 'D': 'Nitrogen'},
        'correct': 'B'
    },
    {
        'question': 'How many chambers does a human heart have?',
        'options': {'A': '2', 'B': '3', 'C': '4', 'D': '5'},
        'correct': 'C'
    },
    {
        'question': 'What is the main function of the roots of a plant?',
        'options': {'A': 'Photosynthesis', 'B': 'Absorption of water and nutrients', 'C': 'Reproduction', 'D': 'Protection'},
        'correct': 'B'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': {'A': 'Venus', 'B': 'Mars', 'C': 'Jupiter', 'D': 'Saturn'},
        'correct': 'B'
    },
    {
        'question': 'What is the process of breaking down food in the stomach called?',
        'options': {'A': 'Absorption', 'B': 'Digestion', 'C': 'Metabolism', 'D': 'Excretion'},
        'correct': 'B'
    },
    {
        'question': 'Which gas is most abundant in our atmosphere?',
        'options': {'A': 'Oxygen', 'B': 'Carbon Dioxide', 'C': 'Nitrogen', 'D': 'Helium'},
        'correct': 'C'
    },
    {
        'question': 'What is the main component of air that we breathe in?',
        'options': {'A': 'Nitrogen', 'B': 'Carbon Dioxide', 'C': 'Oxygen', 'D': 'Hydrogen'},
        'correct': 'C'
    },
    {
        'question': 'How long is one day on Earth?',
        'options': {'A': '12 hours', 'B': '24 hours', 'C': '36 hours', 'D': '48 hours'},
        'correct': 'B'
    },
]


def seed_database(app):
    """Seed the database with questions"""
    with app.app_context():
        # Check if questions already exist
        existing_math = Question.query.filter_by(subject='Math').count()
        existing_science = Question.query.filter_by(subject='Science').count()
        
        if existing_math > 0 and existing_science > 0:
            print("Database already seeded with questions.")
            return
        
        # Add Math questions
        for q_data in MATH_QUESTIONS:
            question = Question(
                subject='Math',
                question_text=q_data['question'],
                option_a=q_data['options']['A'],
                option_b=q_data['options']['B'],
                option_c=q_data['options']['C'],
                option_d=q_data['options']['D'],
                correct_option=q_data['correct'],
                difficulty_level='Medium'
            )
            db.session.add(question)
        
        # Add Science questions
        for q_data in SCIENCE_QUESTIONS:
            question = Question(
                subject='Science',
                question_text=q_data['question'],
                option_a=q_data['options']['A'],
                option_b=q_data['options']['B'],
                option_c=q_data['options']['C'],
                option_d=q_data['options']['D'],
                correct_option=q_data['correct'],
                difficulty_level='Medium'
            )
            db.session.add(question)
        
        db.session.commit()
        print(f"Seeded {len(MATH_QUESTIONS)} Math questions and {len(SCIENCE_QUESTIONS)} Science questions.")
