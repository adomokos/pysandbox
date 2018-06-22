import unittest

from string import Template

class TestStrings(unittest.TestCase):

    def test_string_format_methods(self):
        formatted_string = 'This is one {0} and two {1}'.format(1, 2)
        self.assertEqual("This is one 1 and two 2", formatted_string)

        number_formatted_string = '{:,}'.format(123492424)
        self.assertEqual("123,492,424", number_formatted_string)

    def test_templating(self):
        s = Template('$who likes $what')
        result = s.substitute(who='tim', what='kung pao')
        self.assertEqual('tim likes kung pao', result)

    def test_titlecase_strings(self):
        result = 'this is me'.title()
        self.assertEqual("This Is Me", result)

    def test_split_string(self):
        result = 'this is me'.split()
        self.assertEqual(['this', 'is', 'me'], result)

    def test_join_words(self):
        result = " ".join(['one','two'])
        self.assertEqual('one two', result)

    def test_uppercase_words(self):
        result = 'hello there'.upper()
        self.assertEqual('HELLO THERE', result)
