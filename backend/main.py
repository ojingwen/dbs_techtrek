from google.cloud import firestore, storage
import os 
from flask import Flask
from flask import redirect, url_for, request, make_response, jsonify, render_template
import requests  
import Firestore

# TODO: refactor so that private key is specified in config
# TODO: loop to listen on ip
# TODO: api for front-end to access 
# TODO: structure properly 

# register default configs and blueprints 
app = Flask(__name__)
app.config.from_pyfile("config.py")
app.register_blueprint(Firestore.crud)

# Project ID is determined by the GCLOUD_PROJECT environment variable
# persistent object passed around 
db = firestore.Client()

@app.route('/')
def hello() -> str:
    return "hello world"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)
