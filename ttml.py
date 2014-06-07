from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/event/list')
def event_list():
    return 'Hello World!'

@app.route('/categories')
def categories():
    return 'Hello World!'

@app.route('/event/attend')
def event_attend():
    return 'Hello World!'

@app.route('/event/search')
def event_search():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()