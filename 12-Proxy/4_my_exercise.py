import unittest
from unittest import TestCase


class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'


class ResponsiblePerson:
    def __init__(self, person):
        self.person = person
        self.age = person.age

    def drive(self):
        if self.age < 18:
            return 'too young'
        else:
            return self.person.drive()

    def drink(self):
        if self.age < 18:
            return 'too young'
        else:
            return self.person.drink()

    def drink_and_drive(self):
        return 'dead'


class Evaluate(TestCase):
    def test_exercise(self):
        p = Person(10)
        rp = ResponsiblePerson(p)

        self.assertEqual('too young', rp.drive())
        self.assertEqual('too young', rp.drink())
        self.assertEqual('dead', rp.drink_and_drive())

        rp.age = 20

        self.assertEqual('driving', rp.drive())
        self.assertEqual('drinking', rp.drink())
        self.assertEqual('dead', rp.drink_and_drive())


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
