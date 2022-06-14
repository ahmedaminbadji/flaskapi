
from database.db_config import db
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),unique=True)

    def getById(id):
        return Category.query.filter_by(id=id).first()
    
    def getAll():
        return  Category.query.all()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title
        }