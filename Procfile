web: gunicorn --worker-class sync --workers 4 --bind 0.0.0.0:$PORT --timeout 120 "app:create_app()"
release: python -c "from app import create_app; app = create_app(); from flask import current_app; with app.app_context(): from app.models import db; db.create_all(); from app.seed_questions import seed_database; seed_database(app)"
