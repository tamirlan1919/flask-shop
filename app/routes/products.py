from flask import Blueprint, request, jsonify, render_template, redirect
from app.database.engine import db
from app.database.models import Product, Category

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods = ['GET', 'POST'])
def get_products():
    if request.method == 'POST':
        name = request.form.get('name')
        price = float(request.form.get('price'))
        category_id = int(request.form.get('category_id'))
        products = Product(name = name, price = price, category_id = category_id)
        db.session.add(products)
        db.session.commit()
        return redirect('/products')
    
    products = Product.query.all()
    categories = Category.query.all()
    return render_template('products/list.html', products = products, categories = categories)

@products_bp.route('/delete/<int:id>', methods=['POST'])
def delete_product(id):
    category = Product.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return redirect('/products')

