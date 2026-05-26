"""
WSGI entry point for production deployment
Used by gunicorn or other WSGI servers
"""

from app import create_app
from app.seed_questions import seed_database

app = create_app()

# Seed database on startup if needed
with app.app_context():
    seed_database(app)

if __name__ == "__main__":
    app.run()
