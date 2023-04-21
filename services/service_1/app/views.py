from flask import request
from app import app, db
from app.models import Service1Model

@app.route('/service_1/api_1', methods=['GET'])
def api_1():
    # get data from database
    return {"msg": "Return data to requester"}

@app.route('/service_1/api_2', methods=['POST'])
def api_2():
    example_data = request.get_json()
    value = example_data['key']
    return {"msg": f"Post data with input: {value}"}