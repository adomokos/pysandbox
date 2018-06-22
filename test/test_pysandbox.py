import pysandbox
import unittest

class TestPysandbox(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(pysandbox.say_hello("Attila"), 'Hello, Attila')

