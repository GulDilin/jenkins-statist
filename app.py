from flask import Flask, request, escape
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/')
def print_build_steps():
    data = request.data
    print(data)



if __name__ == '__main__':
    app.run()
