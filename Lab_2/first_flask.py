from flask import Flask, jsonify, request
from werkzeug.routing import BaseConverter, ValidationError

_USERS = {
    '1': 'Fred',
    '2': 'Barney',
    '3': 'Wilma'
}
_IDS = {val: id for id, val in _USERS.items()}

print(_IDS)


class RegistredUser(BaseConverter):
    def to_python(self, value):
        if value in _USERS:
            return _USERS[value]

    def to_url(self, value):
        return _IDS[value]


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.url_map.converters['registred'] = RegistredUser


@app.route('/api', methods=['GET', 'POST', 'DELETE'])
def my_microservice():
    response = jsonify({'Hello': 'World!'})
    return response


""" @app.route('/api/people/<int:person_id>')
def person(person_id):
    return jsonify({'Hello': f'Person {person_id}!'})
 """

@app.route('/api/people/<registred:name>')
def personByName(name):
    return jsonify({'Hello': f'Person {name}!'})


if __name__ == '__main__':
    print(app.url_map)
    app.run()
