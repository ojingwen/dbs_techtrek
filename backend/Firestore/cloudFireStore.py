# this pyfile handles all non-crud operations to firestore
# this is the actual handler to the db doing the read/write; methods called from crud are a wrapper around this 

from flask import Flask
from google.cloud import firestore
import google.cloud.exceptions
from typing import List
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "private.json"

db = firestore.Client()

# collectionName is users
def read(collectionName: str, documentName: str):
    """reads a given document from firebase. returns the dict object unless document not found then returns None. caller has to handle the case of None"""
    # document name is our username
    doc_ref = db.collection(collectionName).document(documentName)
    try:
        doc = doc_ref.get()
        return doc.to_dict()
    except google.cloud.exceptions.NotFound:
        return None

def create(collectionName: str, documentName: str, data: dict):
    """creates the given document in the collection. this operation is idempotent"""
    db.collection(collectionName).document(documentName).set(data)


def update(collectionName: str, documentName: str, data: dict):
    """update the given document in the collection. this operation is NON-idempotent"""
    db.collection(collectionName).document(documentName).update(data)


def delete(collectionName: str, documentName: str):
    """deletes the given document in the collection. this operation is idempotent"""
    db.collection(collectionName).document(documentName).delete()
