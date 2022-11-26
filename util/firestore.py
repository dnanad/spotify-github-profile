from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin
import json
import os
from base64 import b64decode
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_firestore_db():
    firebase_config = os.getenv("FIREBASE")
    print(b64decode(firebase_config))
    firebase_dict = json.loads(b64decode(firebase_config))

    cred = credentials.Certificate(firebase_dict)
    firebase_admin.initialize_app(cred)
    print('ufff')
    return firestore.client()
