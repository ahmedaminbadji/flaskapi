from flask import Flask
from flask_migrate import Migrate
from database.db_config import db
from routes.product_blueprint import product_bp
from routes.category_blueprint import category_bp
from routes.shop_blueprint import shop_bp
from routes.address_blueprint import address_bp
# from routes.shop_bp import shop_bp
# from routes.category_bp import category_bp

#Init APP

app = Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))

app.config.from_object('config')
#['SQLALCHEMY_DATABASE_URI'] = "postgres+psycopg2://user:pass@localhost/db_name"


migrate = Migrate(app, db)
db.init_app(app)
app.register_blueprint(product_bp, url_prefix='/products') 
app.register_blueprint(address_bp, url_prefix='/addresses') 
app.register_blueprint(category_bp, url_prefix='/categories') 
app.register_blueprint(shop_bp, url_prefix='/shops') 


@app.route('/')
def index():
    return "RESTFUL API"

# Run Server

if __name__ == '__main__':
    app.run(debug=True)
    