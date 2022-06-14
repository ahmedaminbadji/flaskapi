import sys
from flask import request, abort
from flask import jsonify
from models.Shop import Shop

def store():
    try:
        name = request.json['name']
        address =  request.json['address']
        shop = Shop(name,address)
    except:
        return jsonify({"Error":"Missing Data"}),400
    return shop.store()

def getById(shop_id):
    try:
        return Shop.getById(shop_id).serialize
    except:
        return jsonify({"Error":"Not found"}),404
        
def show():
    return jsonify([i.serialize for i in Shop.getAll()])


def update(shop_id):
    try:
        name = request.json['name']
        address =  request.json['address']
        product = Shop(name,address)
    except:
        return jsonify({"Error":"Missing Data"}),400
    return product.update(shop_id).serialize


def destroy(shop_id):
     return Shop.destroy(shop_id).serialize