import unittest
import math

"""
  * Instance methods need a class instance and can access the instance through self.
  * Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.
  * Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.
  * Static and class methods communicate and (to a certain degree) enforce developer intent about class design. This can have maintenance benefits.
"""

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        """For printing purposes"""
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


class TestCalculator(unittest.TestCase):

    def test_calculator_add_method_returns_correct_result(self):
        self.margherita = Pizza(['mozzarella','tomatoes'])
        result = repr(self.margherita)
        self.assertEqual("Pizza(['mozzarella', 'tomatoes'])", result)

    def test_class_method_can_construct_an_instance(self):
        result = repr(Pizza.prosciutto())
        self.assertEqual("Pizza(['mozzarella', 'tomatoes', 'ham'])", result)

    def test_static_method(self):
        result = int(Pizza.circle_area(3))
        self.assertEqual(28, result)
