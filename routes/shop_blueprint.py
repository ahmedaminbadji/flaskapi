from flask import Blueprint
from controllers.ShopController import store,getById,show,destroy,update
shop_bp = Blueprint('shop_bp', __name__)
shop_bp.route('/create', methods=['POST'])(store)
shop_bp.route('/<int:shop_id>', methods=['GET'])(getById)
shop_bp.route('/', methods=['GET'])(show)
shop_bp.route('/edit/<int:shop_id>', methods=['PUT'])(update)
shop_bp.route('/<int:shop_id>', methods=['DELETE'])(destroy)