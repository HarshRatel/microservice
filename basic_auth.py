from flask import Flask, request, jsonify, url_for
from werkzeug.routing import BaseConverter, ValidationError


class RegisterdUser(BaseConverter):
	def to_python(self, value):
		if value in _USERS:
			return _USERS[value]
		raise ValidationError

	def to_url(self, value):
		return _IDS[value]

app = Flask(__name__)
app.url_map.converters["registered"] = RegisterdUser

@app.route("/")
def auth():
	print("the raw auth header")
	print(request.environ["HTTP_AUTHORIZATION"])
	print("Flask's auth header")
	print(request.authorization)
	return jsonify({'success': "yes"})

_USERS = {'1':'Taker', '2':'Freya'}
_IDS = {val: id for id, val in _USERS.items()}

@app.route("/person/<registered:name>")
def person(name):
	print(url_for('person', name="Taker"))
	return jsonify({"hello" : name})

if __name__ == "__main__":
	app.run()