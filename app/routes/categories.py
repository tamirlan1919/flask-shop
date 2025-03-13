from flask import Blueprint, request, jsonify, render_template
from app.database.engine import db
from app.database.models import Category

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/', methods = ['GET', 'POST'])
def get_categories():
    if request.method == 'POST':
        name = request.form.get('name')
        category = Category(name = name)
        db.session.add(category)
        db.session.commit()
        return jsonify({
            'message': 'Category added',
            'id': category.id
            })
    
    categories = 2
    return render_template('categories/list.html', categories = categories )