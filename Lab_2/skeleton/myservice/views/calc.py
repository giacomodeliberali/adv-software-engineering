from flask import jsonify
from flakon import JsonBlueprint
import calculator as calculator

calc = JsonBlueprint('calc', __name__)


@calc.route('/calc/sum/<int:a>/<int:b>')
def sum(a, b):
    return jsonify({'result': calculator.sum(a, b)})


@calc.route('/calc/divide/<int:a>/<int:b>')
def divide(a, b):
    return jsonify({'result': calculator.divide(a, b)})
