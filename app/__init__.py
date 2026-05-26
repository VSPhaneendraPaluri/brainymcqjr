from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import db

def create_app():
    """Application factory"""
    app = Flask(__name__, 
                template_folder='templates', 
                static_folder='static')
    
    # Configuration
    import os
    db_uri = os.environ.get('DATABASE_URL', 'sqlite:///mcq_quiz.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    
    # Initialize database
    db.init_app(app)
    
    # Security headers middleware
    @app.after_request
    def set_security_headers(response):
        # Enforce HTTPS
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        # Prevent clickjacking
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        # Prevent MIME type sniffing
        response.headers['X-Content-Type-Options'] = 'nosniff'
        # Enable XSS protection
        response.headers['X-XSS-Protection'] = '1; mode=block'
        # Content Security Policy
        response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline';"
        # Referrer Policy
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        # Permissions Policy
        response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
        return response
    
    # Redirect HTTP to HTTPS in production
    @app.before_request
    def before_request():
        from flask import request, redirect
        # Only enforce in production (not localhost)
        if not app.debug and request.headers.get('X-Forwarded-Proto', 'http') != 'https':
            return redirect(request.url.replace('http://', 'https://', 1), code=301)
    
    # Register blueprints
    from app.routes import main_bp, auth_bp, quiz_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(quiz_bp)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app
