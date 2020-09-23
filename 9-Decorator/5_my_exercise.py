import unittest
from unittest import TestCase


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return 'A circle of radius {}'.format(self.radius)


class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return 'A square with side {}'.format(self.side)


class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        if isinstance(self.shape, Square):
            return
        self.shape.resize(factor)

    def __str__(self):
        return '{} has the color {}'.format(self.shape, self.color)


class Evaluate(TestCase):
    def test_circle(self):
        circle = ColoredShape(Circle(5), 'red')
        self.assertEqual(
            'A circle of radius 5 has the color red',
            str(circle)
        )
        circle.resize(2)
        self.assertEqual(
            'A circle of radius 10 has the color red',
            str(circle)
        )

    def test_no_resize_in_square(self):
        square = Square(4)
        r = getattr(square, 'resize', None)
        self.assertFalse(callable(r),
                         'Please do not add resize() to Square')

    def test_square(self):
        square = ColoredShape(Square(2), 'blue')
        self.assertEqual(
            'A square with side 2 has the color blue',
            str(square)
        )
        square.resize(2)
        self.assertEqual(
            'A square with side 2 has the color blue',
            str(square)
        )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
