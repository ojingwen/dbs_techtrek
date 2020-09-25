# this file provides the actual api endpoints for front-end to hit
from flask import Blueprint, request, jsonify, make_response, render_template, url_for, redirect
from werkzeug.exceptions import NotFound, InternalServerError
from . import cloudFireStore    
import datetime 
crud = Blueprint('crud', __name__)

@crud.route('/create', methods = ['PUT'])
def create():
    """gets the json object and creates the document from the provided type and id. returns 200 if ok else 500"""
    d = request.args().to_dict()
    data = request.get_json()
    try: 
        cloudFireStore.create(data, **d)
        resp = jsonify(success=True)
        return resp
    except:
        raise InternalServerError("The requested operation could not be performed")

@crud.route('/read', methods = ['GET'])
def read():
    """reads data from db and returns it as a json object else raises 404; extracts args from request params"""
    d = request.args.to_dict()
    data = cloudFireStore.read(**d)
    if data == None:
        raise NotFound("The document you are requesting could not be found in the database")
    resp = make_response(data)
    resp.headers['Access-Control-Allow-Origin'] = '*' # do this for everything 
    return resp 

@crud.route('/update', methods = ['POST'])
def update():
    """parses a json dict and creates an object in db; returns 200 if ok else 500"""
    d = request.args.to_dict()
    data = request.get_json()
    try:
        cloudFireStore.update(data = data, **d) 
        resp = jsonify(success=True)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except:
        raise InternalServerError("The requested operation could not be performed")

@crud.route('/delete', methods = ['GET'])
def delete():
    """deletes the given document under collection"""
    d = request.args.to_dict() 
    print(d)
    cloudFireStore.delete(**d)
    resp = jsonify(success=True)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp 