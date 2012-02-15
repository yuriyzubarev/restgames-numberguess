import os
import unittest
import tempfile

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import game

class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.app = game.app.test_client()

    def tearDown(self):
        pass

    def test1(self):
        response = self.app.get('/')
        assert 'Hello World!' in response.data

    def test_should_start_new_game(self):
        response = self.app.post('/start')
        self.assertTrue(False)

    def test_should_return_game_info(self):
        response = self.app.get('/123')
        self.assertTrue(False)

    def test_should_return_too_high(self):
        response = self.app.put('/123')
        self.assertTrue(False)

    def test_should_return_too_low(self):
        response = self.app.put('/123')
        self.assertTrue(False)

    def test_should_return_match(self):
        response = self.app.put('/123')
        self.assertTrue(False)

    def test_should_end_inprogress_game(self):
        response = self.app.put('/123/end')
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
