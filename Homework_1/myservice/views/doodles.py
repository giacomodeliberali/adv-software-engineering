from flakon import JsonBlueprint
from flask import request, jsonify, abort
from myservice.classes.poll import Poll, NonExistingOptionException, UserAlreadyVotedException

doodles = JsonBlueprint('doodles', __name__)

_ACTIVEPOLLS = {}  # list of created polls
_POLLNUMBER = 0  # index of the last created poll


@doodles.route('/doodles', methods=['GET', 'POST'])
def all_polls():

    if request.method == 'POST':
        result = create_doodle(request)

    elif request.method == 'GET':
        result = get_all_doodles(request)

    return result


@doodles.route('/doodles/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def single_poll(id):
    global _ACTIVEPOLLS
    result = ""

    exist_poll(id)  # check if the Doodle is an existing one

    if request.method == 'GET':  # retrieve a poll
        result = jsonify(_ACTIVEPOLLS[id].serialize())

    elif request.method == 'DELETE':
        result = jsonify({'winners': _ACTIVEPOLLS[id].get_winners()})
        del _ACTIVEPOLLS[id]

    elif request.method == 'PUT':
        vote(id, request)
        result = jsonify({'winners': _ACTIVEPOLLS[id].get_winners()})

    return result


@doodles.route('/doodles/<int:id>/<person>', methods=['GET', 'DELETE'])
def person_poll(id, person):

    global _ACTIVEPOLLS
    result = ""

    exist_poll(id)

    if request.method == 'GET':
        result = jsonify(
            {'votedoptions': _ACTIVEPOLLS[id].get_voted_options(person)})
    if request.method == 'DELETE':
        result = jsonify(
            {'removed': _ACTIVEPOLLS[id].delete_voted_options(person)})

    return result


def vote(id, request):
    global _ACTIVEPOLLS
    result = ""

    try:
        data = request.get_json()
        _ACTIVEPOLLS[id].vote(data['person'], data['option'])
        result = _ACTIVEPOLLS[id].get_winners()

    except UserAlreadyVotedException:
        abort(400)  # Bad Request
    except NonExistingOptionException:
        abort(400)

    return result


def create_doodle(request):
    global _ACTIVEPOLLS, _POLLNUMBER

    data = request.get_json()

    _POLLNUMBER += 1

    newPoll = Poll(
        _POLLNUMBER,
        data['title'],
        data['options']
    )

    _ACTIVEPOLLS[_POLLNUMBER] = newPoll

    return jsonify({
        'pollnumber': _POLLNUMBER
    })


def get_all_doodles(request):
    global _ACTIVEPOLLS
    return jsonify(activepolls=[e.serialize() for e in _ACTIVEPOLLS.values()])


def exist_poll(id):
    global _ACTIVEPOLLS
    if int(id) > _POLLNUMBER:
        abort(404)  # error 404: Not Found, i.e. wrong URL, resource does not exist
    elif not(id in _ACTIVEPOLLS):
        abort(410)  # error 410: Gone, i.e. it existed but it's not there anymore
