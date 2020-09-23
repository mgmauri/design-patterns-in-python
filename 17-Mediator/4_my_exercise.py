import unittest


class Participant:
    def __init__(self, mediator):
        self.mediator = mediator
        self.value = 0
        self.mediator.elements.append(self)

    def say(self, value):
        self.mediator.update_values(self, value)


class Mediator:
    def __init__(self):
        self.elements = list()

    def update_values(self, element, value):
        for logged_element in self.elements:
            if logged_element != element:
                logged_element.value += value


class FirstTestSuite(unittest.TestCase):
    def test(self):
        m = Mediator()
        p1 = Participant(m)
        p2 = Participant(m)

        self.assertEqual(0, p1.value)
        self.assertEqual(0, p2.value)

        p1.say(2)

        self.assertEqual(0, p1.value)
        self.assertEqual(2, p2.value)

        p2.say(4)

        self.assertEqual(4, p1.value)
        self.assertEqual(2, p2.value)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
