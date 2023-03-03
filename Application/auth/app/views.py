from flask import jsonify
from app import app

success = 200
fail = 400

# API test
@app.route('/auth/', methods=['GET'])
def get_hello_auth():
    return jsonify({'message': f'Hello from auth API'}), success