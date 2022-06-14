from database.db_config import db
class Shop(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),unique=True, nullable=False)
    address = db.Column(db.Integer, db.ForeignKey('addresses.id'))


    def __init__(self,name,address):
        self.name = name
        self.address = address

    def store(self):
        db.session.add(self)
        db.session.commit()
        return self.serialize

    def getById(id):
        return Shop.query.filter_by(id=id).first()
    
    def destroy(id):
        shop = Shop.getById(id)
        db.session.delete(shop)
        db.session.commit()
        return shop
        
    def update(self,id):
        shop = Shop.getById(id)
        shop.name = self.name
        shop.address = self.address
        db.session.commit()
        return shop

    def getAll():
        return  Shop.query.all()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }