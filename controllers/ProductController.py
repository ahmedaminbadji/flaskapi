import sys
from flask import request, abort
from flask import jsonify
from models.Product import Product



def store():
    try:
        name = request.json['name']
        description =  request.json['description']
        price = request.json['price']
        categories = request.json['categories']
    except:
        return jsonify({"Error":"Missing Data"}),400
    product = Product(name,description,price,categories)
    return product.store()

def getById(product_id):
    try:
        return Product.getById(product_id).serialize
    except:
        return jsonify({"Error":"Not found"}),404

def show():
    return jsonify([i.serialize for i in Product.getAll()])
def update(product_id):
    try:
        name = request.json['name']
        description =  request.json['description']
        price = request.json['price']
    except:
        return jsonify({"Error":"Missing Data"}),400
    product = Product(name,description,price)
    return product.update(product_id).serialize
def destroy(product_id):
     return Product.destroy(product_id).serialize