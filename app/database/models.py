from app.database.engine import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Float, nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable = False)
    category = db.relationship('Category', backref=db.backref('products'))

