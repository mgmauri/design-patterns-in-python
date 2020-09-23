import unittest
from unittest import TestCase
from collections import Iterable


class ValueCounter(Iterable):
    @property
    def sum(self):
        result = 0
        for instance in self:
            for value in instance:
                result += value
        return result


class SingleValue(ValueCounter):
    """Single Value class"""

    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, ValueCounter):
    pass


class Evaluate(TestCase):
    def test_exercise(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
