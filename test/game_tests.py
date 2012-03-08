import os
import unittest
import tempfile
import json

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import game

class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.app = game.app.test_client()

    def tearDown(self):
        pass

    def test_should_start_new_game(self):
        response = self.app.post('/start')
        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.headers["Location"])
        self.assertEqual('/123', response.headers["Location"][-4:])

    def test_should_return_game_info(self):
        response = self.app.get('/123')
        self.assertEqual(200, response.status_code)
        self.assertEqual(json.dumps({"name": "Number Guess", "id": 123}, indent = 2), response.data)

    def test_should_return_too_high(self):
        response = self.app.post('/123/guesses', data = dict(guess=7))
        self.assertEqual(200, response.status_code)

    def test_should_return_too_low(self):
        response = self.app.post('/123/guesses', data = dict(guess=3))
        self.assertEqual(200, response.status_code)

    def test_should_return_match(self):
        response = self.app.post('/123/guesses', data = dict(guess=5))
        self.assertEqual(200, response.status_code)

    def test_should_end_inprogress_game(self):
        response = self.app.post('/123/end')
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()
