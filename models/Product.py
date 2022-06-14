
from database.db_config import db
from models.product_in_category import product_in_category
from models.Category import Category

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    categories = db.relationship('Category', secondary=product_in_category, lazy='subquery',
        backref=db.backref('productscats', lazy=True))


    def __init__(self,name,description,price,categories):
        self.name = name
        self.description = description
        self.price = price
        for category in categories:
            self.categories.append(Category.getById(category))
            

    def store(self):
        db.session.add(self)
        db.session.commit()
        return self.serialize

    def getById(id):
        return Product.query.filter_by(id=id).first()
    
    def destroy(id):
        product = Product.getById(id)
        db.session.delete(product)
        db.session.commit()
        return product
        
    def update(self,id):
        product = Product.getById(id)
        product.name = self.name
        product.description = self.description
        product.price = self.price
        db.session.commit()
        return product

    def getAll():
        return  Product.query.all()
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'categories' :  [i.serialize for i in self.categories]
        }

       