from flask import Blueprint
from controllers.CategoryController import getById,show

category_bp = Blueprint('category_bp', __name__)
category_bp.route('/<int:category_id>', methods=['GET'])(getById)
category_bp.route('/', methods=['GET'])(show)