import sys
from flask import request, abort
from flask import jsonify
from models.Category import Category


def getById(category_id):
    try:
        return Category.getById(category_id).serialize
    except:
        return jsonify({"Error":"Not found"}),404
        
def show():
    return jsonify([i.serialize for i in Category.getAll()])
