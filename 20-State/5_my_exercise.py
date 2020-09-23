import unittest


class CombinationLock:
    def __init__(self, combination):
        """

        """
        self.combination = ''.join([str(s) for s in combination])
        self.status = 'LOCKED'
        self.str_input = ''

    def reset(self):
        self.status = 'LOCKED'
        self.str_input = ''

    def enter_digit(self, digit):
        self.str_input += str(digit)
        if self.combination.startswith(self.str_input):
            self.status = 'OPEN' if self.str_input == self.combination else self.str_input
        else:
            self.status = 'ERROR'


class FirstTestSuite(unittest.TestCase):
    def test_success(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(3)
        self.assertEqual('123', cl.status)
        cl.enter_digit(4)
        self.assertEqual('1234', cl.status)
        cl.enter_digit(5)
        self.assertEqual('OPEN', cl.status)

    def test_failure(self):
        cl = CombinationLock([1, 2, 3])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(5)
        self.assertEqual('ERROR', cl.status)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
