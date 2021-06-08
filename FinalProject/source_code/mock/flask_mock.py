import json
import random

from flask import Flask, jsonify, request

app = Flask(__name__)

MOCK_DATA = {}
MOCK_DATA['user_name']= ''
user_id_seq = 1


@app.route('/', methods=['GET'])
def get_root():
    return jsonify('yxadi'), 400


@app.route('/vk_id/<username>', methods=['GET'])
def get_user(username):
    if username in MOCK_DATA['user_name']:
        vk_id = random.randint(0, 100)
        return jsonify({'vk_id': vk_id}), 200
    else:
        return jsonify({}), 404

@app.route('/vk_id/post/user', methods=['POST'])
def post_user():
    user_name = json.loads(request.data)['name']
    MOCK_DATA['user_name'] = user_name
    return jsonify({'name':user_name}),200


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'OK, exiting'), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083, debug=True)
