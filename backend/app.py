from flask import Flask, jsonify, request
# import database as DB
from flask_cors import CORS
import json
import openAi as AI

app = Flask(__name__)
CORS(app)

@app.route('/')
def start():  
    print("connection has begun")  
    return "Connection Started"

@app.route('/input', methods = ['POST'])
def get_input():
    data = request.data
    string_dict = json.loads(data)
    user_input = string_dict['input']
    coords = AI.findCoordinates(AI.prepCoordinates(user_input))
    if not coords:
        response = jsonify({'coords': False})
    else:
        response = jsonify({'coords': coords})
    return response

if __name__ == '__main__':
    app.run()