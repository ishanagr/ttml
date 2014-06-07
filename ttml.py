from flask import Flask
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
app = Flask(__name__)

import database
from models import *
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

admin = Admin(app, name='Can lah!')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Event, db.session))
admin.add_view(ModelView(Category, db.session))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
