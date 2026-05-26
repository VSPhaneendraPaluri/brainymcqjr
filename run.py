"""
MCQ Quiz Master - Main Application Entry Point
Run this file to start the web server with HTTPS support

For production on Render, use: gunicorn "app:create_app()"
For local development, run this file directly
"""

from app import create_app
from app.seed_questions import seed_database
import os

# Create Flask app
app = create_app()

# Seed database with questions on first run
with app.app_context():
    seed_database(app)

if __name__ == '__main__':
    print("""
    ╔═══════════════════════════════════════════════════════╗
    ║  MCQ Quiz Master - Interactive Learning Platform     ║
    ║  Class 3-5 Mathematics & Science Quiz                ║
    ║  (HTTPS Enabled)                                      ║
    ╚═══════════════════════════════════════════════════════╝
    
    🚀 Starting MCQ Quiz Master...
    📚 Navigate to: https://localhost:5000
    
    Note: You may see a certificate warning - this is normal
    for self-signed certificates in development.
    
    Features:
    ✓ 25 Mathematics + 25 Science MCQ Questions
    ✓ Secure User Login & Registration
    ✓ 60-minute Timed Quiz
    ✓ Score History & Progress Tracking
    ✓ Subject-wise Question Segregation
    ✓ Responsive Design for All Devices
    ✓ HTTPS Enabled for Security
    
    Press Ctrl+C to stop the server
    """)
    
    # Check if running in production
    is_production = os.environ.get('FLASK_ENV') == 'production'
    
    if not is_production:
        # Development mode with SSL certificates
        cert_file = 'cert.pem'
        key_file = 'key.pem'
        
        if os.path.exists(cert_file) and os.path.exists(key_file):
            # Use SSL certificates
            ssl_context = (cert_file, key_file)
            print(f"🔒 Using SSL certificates: {cert_file}, {key_file}")
        else:
            # Use adhoc SSL (generates on the fly)
            ssl_context = 'adhoc'
            print("🔒 Using adhoc SSL (self-signed)")
        
        # Run development server with HTTPS
        app.run(
            debug=True, 
            host='0.0.0.0', 
            port=5000,
            ssl_context=ssl_context
        )
    else:
        # Production mode - HTTPS handled by reverse proxy (Render)
        app.run(
            debug=False,
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 5000))
        )
