from flask import Flask
from app.config import Config
from app.database.engine import db
from app.routes.categories import categories_bp
from app.routes.products import products_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        from app.database import models  # Импорт моделей, чтобы они были зарегистрированы
        db.create_all()

    app.register_blueprint(categories_bp, url_prefix='/categories')
    app.register_blueprint(products_bp, url_prefix = '/products')
    return app