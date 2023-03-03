import requests
from app import app

@app.route('/')
def index():
    test = requests.get('http://flask-booking:8002/booking/')
    return test.json()

@app.route('/login')
def login():
    test = requests.get('http://flask-auth:8001/auth/')
    return test.json()