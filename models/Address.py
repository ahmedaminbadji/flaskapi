from database.db_config import db
from models.Shop import Shop
class Address(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer,primary_key=True)
    street = db.Column(db.String(150),unique=True, nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    country = db.Column(db.String(3), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    shop = db.relationship('Shop',backref='shopaddress',uselist=False)


    def __init__(self,street,city,state,country,zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.zip_code = zip_code

    def store(self):
        db.session.add(self)
        db.session.commit()
        return self.serialize

    def getById(id):
        return Address.query.filter_by(id=id).first()
    
    def destroy(id):
        address = Address.getById(id)
        db.session.delete(address)
        db.session.commit()
        return address
        
    def update(self,id):
        address = Address.getById(id)
        address.street = self.street
        address.city = self.city
        address.state = self.state
        address.country = self.country
        address.zip_code = self.zip_code 
        db.session.commit()
        return address

    def getAll():
        return  Address.query.all()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'zip_code': self.zip_code
        }