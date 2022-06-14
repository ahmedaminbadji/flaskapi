from flask import Blueprint
from controllers.ProductController import store,getById,show,destroy,update
product_bp = Blueprint('product_bp', __name__)
product_bp.route('/create', methods=['POST'])(store)
product_bp.route('/<int:product_id>', methods=['GET'])(getById)
product_bp.route('/', methods=['GET'])(show)
product_bp.route('/edit/<int:product_id>', methods=['PUT'])(update)
product_bp.route('/<int:product_id>', methods=['DELETE'])(destroy)