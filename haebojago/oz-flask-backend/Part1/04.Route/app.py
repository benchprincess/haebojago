from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Mr.my Yesterday!"

@app.route('/about')
def about():
    return "Hello, This is the about Page!"

@app.route('/company')
def company():
    return "This is the company Page!"

@app.route('/number/<int:number>')
def number(number):
    return f"number : {number}"

@app.route('/user/<username>')
def user_profile(username):
    return f"Username : {username}"

@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url=url, data=data)

    return response

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)

    if request.method == "GET":
        print("GET method")
    
    if request.method == "POST":
        print("POST method" , request.data)

    return Response("Successfully submitted", status=200)

if __name__ == "__main__":
    app.run(debug=True)

