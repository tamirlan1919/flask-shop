from flask import Blueprint, request, jsonify, render_template, redirect
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
        return redirect('/categories')
    
    categories = Category.query.all()
    return render_template('categories/list.html', categories = categories )

@categories_bp.route('/delete/<int:id>', methods=['POST'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return redirect('/categories')

