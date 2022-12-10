from flask import Flask,request,jsonify
import numpy as np
import model_handler
import db_handler

import config
import utils

MODEL_PATH = config.MODEL_PATH
conn = db_handler.get_db_connection()

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello, World!'

@app.route('/user')
def user():
    return 'Hello, User!'

@app.route('/predict', methods=['POST'])
def predict():  
    params = request.get_json()
    input_list = [float(value) for key, value in params.items()]
    input_list = np.array(input_list)

    result = model_handler.predict_value(MODEL_PATH, input_list, utils.train_columns)
    return f'{result}'

@app.route('/save_history', methods=['POST'])
def save_historys():  
    params = request.get_json()
    hitory_input_tuple, feature_history_input_tuple = db_handler.split_data(params)
    print(feature_history_input_tuple)
    db_handler.insert_history(conn, hitory_input_tuple)
    db_handler.insert_feature_history(conn, feature_history_input_tuple)
    
    return 'Success for save history'

if __name__ == '__main__':
    app.run(debug=True)