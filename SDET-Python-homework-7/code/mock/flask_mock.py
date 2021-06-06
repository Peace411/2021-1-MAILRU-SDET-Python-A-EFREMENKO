import json
import threading

from flask import Flask, jsonify, request

import settings

app = Flask(__name__)

SURNAME_DATA = {}
mock_data = {}

user_id_seq = 1


@app.route('/', methods=['GET'])
def get_root():
    return jsonify('yxadi'), 400


@app.route('/get_surname/<name>', methods=['GET'])
def get_user_surname(name):
    if surname := SURNAME_DATA.get('name'):
        return jsonify(surname), 200

    else:
        return jsonify(f'Surname for user {name} not fount'), 404


@app.route('/post_name', methods=['POST'])
def post_user():
    global user_id_seq
    user_name = json.loads(request.data)['name']
    if user_name not in mock_data:
        mock_data[user_name] = user_id_seq
        data = {'user_id': user_id_seq, 'name': user_name}
        user_id_seq += 1
        return jsonify(data), 201
    else:
        return jsonify(f'User name {user_name} already exists: if {mock_data[user_name]}'), 400


@app.route('/get_user_name/<name>', methods=['GET'])
def get_user(name):
    if mock_data.get('name') == name:
        return jsonify(mock_data['name']), 200
    else:
        return jsonify(f'User name {name} already exists: if {mock_data["name"]}'),400


@app.route('/post_surname/<name>', methods=['POST'])
def post_surname(name):
    surname = json.loads(request.data)['surname']
    SURNAME_DATA[name] = surname
    return jsonify(surname), 201


@app.route('/put_surname/<name>', methods=['PUT'])
def put_surname(name):
    surname = json.loads(request.data)['surname']
    if name in mock_data:
        SURNAME_DATA[name] = surname
        return jsonify(surname), 200
    else:
        return jsonify(f'User name {name} already exists:'), 400


@app.route('/delete_surname/<name>', methods=['DELETE'])
def delete_surname(name):
    surname = json.loads(request.data)['surname']
    if name in mock_data:
        data = SURNAME_DATA.popitem()
        return jsonify(data), 204
    else:
        return jsonify(f'User name {name} or surname {surname }already exists: if {mock_data}'), 400


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'OK, exiting'), 200
