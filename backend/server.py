# from typing import Optional
# from fastapi import FastAPI
# from starlette.responses import JSONResponse

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/predict/{predict_values}")
# def read_item(predict_values: int, params: Optional[str] = None): # Optional는 Query
#     return {"predict_values": predict_values, "param": params}

# @app.post("/test")
# def read_item(value : Item):
#     print(value)
#     a = dict(value)
#     return JSONResponse(a)

from flask import Flask,request,jsonify
import numpy as np
import model_handler
import config
import utils

MODEL_PATH = config.MODEL_PATH

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

if __name__ == '__main__':
    app.run(debug=True)