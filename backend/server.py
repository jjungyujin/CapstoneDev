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

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello, World!'

@app.route('/user')
def user():
    return 'Hello, User!'

@app.route('/test', methods=['GET', 'POST'])
def test():  
    # print(request.is_json)
    params = request.get_json()
    val1 = params['value1']
    val2 = params['value2']
    add = int(val1) + int(val2)
    print(add)
    return f'{add}'

if __name__ == '__main__':
    app.run(debug=True)