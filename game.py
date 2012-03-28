from flask import Flask, jsonify, request
import os

controller = Flask(__name__)

@controller.route('/')
def hello_world():
    return 'Number Guess'

@controller.route('/start', methods = ['POST'])
def start_game():
    response = controller.make_response("Started")
    response.status_code = 201
    response.headers["Location"] = "/123"
    return response

@controller.route('/<int:game_id>')
def game_info(game_id):
    return jsonify(name = "Number Guess", id = game_id)

@controller.route('/<int:game_id>/guesses', methods = ['POST'])
def make_guess(game_id):
    guess = request.form['guess']
    return guess

@controller.route('/<int:game_id>/end', methods = ['POST'])
def end_game(game_id):
    return "Ended"


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    controller.run(host = '0.0.0.0', port = port, debug = True)


