from flask import Flask
from flask import request
from flask import jsonify
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from marshmallow import Serializer, fields

app = Flask(__name__)
#app.debug = True

import database
import json
from models import *
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/event/list')
def event_list():
	category_id = request.args.get('category_id')
	if category_id:
		result = db.session.query(Event).filter_by(category_id=category_id).all()
	else:
		result = db.session.query(Event).all()
	result_list =  []
	for i in result:
		result_list.append(i.to_json())
	return json.dumps(result_list)

@app.route('/categories')
def categories_show():
	result = db.session.query(Category).all()
	result_list =  []
	for i in result:
		result_list.append(i.to_json())
	return json.dumps(result_list)

@app.route('/event/attend', methods=['GET', 'POST'])
def event_attend():
	if request.method == 'POST':
		event_id = request.form['event_id']
		user_id = request.form['user_id']
		if event_id and user_id:
			attend = Attend(event_id=event_id, user_id=user_id)
			db.session.add(attend)
			db.session.commit()
	return 'Fuck yeah'

@app.route('/users/list')
def users_show():
  result = db.session.query(User).all()
  result_list =  []
  for i in result:
  	result_list.append(i.to_json())
  return json.dumps(result_list)

@app.route('/event/search')
def event_search():
    return 'Hello World!'

admin = Admin(app, name='Can lah!')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Event, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Attend, db.session))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
