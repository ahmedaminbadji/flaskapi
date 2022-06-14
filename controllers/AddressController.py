import sys
from flask import request, abort
from flask import jsonify
from models.Address import Address

def store():
    try:
        street = request.json['street']
        city =  request.json['city']
        state = request.json['state']
        country = request.json['country']
        zip_code = request.json['zip_code']
    except:
        return jsonify({"Error":"Missing Data"}),400
    address = Address(street,city,state,country,zip_code)
    return address.store()

def getById(address_id):
    try:
        return Address.getById(address_id).serialize
    except:
        return jsonify({"Error":"Not found"}),404
def show():
    return jsonify([i.serialize for i in Address.getAll()])

def update(address_id):
    try:
        street = request.json['street']
        city =  request.json['city']
        state = request.json['state']
        country = request.json['country']
        zip_code = request.json['zip_code']
    except:
        return jsonify({"Error":"Missing Data"}),400
    address = Address(street,city,state,country,zip_code)
    return address.update(address_id).serialize

def destroy(address_id):
     return Address.destroy(address_id).serialize