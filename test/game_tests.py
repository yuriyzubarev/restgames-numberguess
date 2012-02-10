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
        rv = self.app.get('/')
        assert 'Hello World!' in rv.data

if __name__ == '__main__':
    unittest.main()