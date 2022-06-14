from flask import Blueprint
from controllers.AddressController import store,getById,show,destroy,update
address_bp = Blueprint('address_bp', __name__)
address_bp.route('/create', methods=['POST'])(store)
address_bp.route('/<int:address_id>', methods=['GET'])(getById)
address_bp.route('/', methods=['GET'])(show)
address_bp.route('/edit/<int:address_id>', methods=['PUT'])(update)
address_bp.route('/<int:address_id>', methods=['DELETE'])(destroy)