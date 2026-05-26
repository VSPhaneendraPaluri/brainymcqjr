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
    
    # Handle PostgreSQL connection string format from Render
    if db_uri.startswith('postgres://'):
        db_uri = db_uri.replace('postgres://', 'postgresql://', 1)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    
    # Session configuration
    is_production = os.environ.get('FLASK_ENV') == 'production'
    app.config['SESSION_COOKIE_SECURE'] = is_production  # Only send over HTTPS in production
    app.config['SESSION_COOKIE_HTTPONLY'] = True  # No JavaScript access
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # CSRF protection
    app.config['PERMANENT_SESSION_LIFETIME'] = 86400  # 24 hours
    
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
        # Only enforce in production (not localhost) and only for GET requests
        # Don't redirect POST/PUT/DELETE to avoid losing form data
        if not app.debug and request.method == 'GET':
            x_forwarded_proto = request.headers.get('X-Forwarded-Proto', 'http')
            if x_forwarded_proto != 'https' and 'localhost' not in request.host:
                url = request.url.replace('http://', 'https://', 1)
                return redirect(url, code=301)
    
    # Register blueprints
    from app.routes import main_bp, auth_bp, quiz_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(quiz_bp)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app
