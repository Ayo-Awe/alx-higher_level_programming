#!/usr/bin/python3
"""Square Test Module
"""
import unittest
from unittest.mock import patch
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """TestSquareClass
    """

    def test_create_square(self):
        """test_create_squaresfunction
        """
        # Create new instance of rectangle
        sqr = Square(10, 20, 3, 2)

        self.assertEqual(sqr.area(), 100)
        self.assertEqual(sqr.id, 2)
        self.assertEqual(sqr.x, 20)
        self.assertEqual(sqr.y, 3)

        self.assertEqual(str(sqr), "[Square] (2) 20/3 - 10")

        # Type validations
        with self.assertRaises(ValueError) as error:
            sqr.x = -2
        self.assertEqual("x must be >= 0", str(error.exception))

        with self.assertRaises(TypeError) as error:
            sqr.x = 3.2
        self.assertEqual("x must be an integer", str(error.exception))

    def test_string_representation(self):
        """test_string_representation function
        Tests the __str__ function
        """

        sqr_1 = Square(1, 3, 2, 8)
        sqr_2 = Square(3, 2, 0, 2)

        self.assertEqual("[Square] (8) 3/2 - 1", str(sqr_1))
        self.assertEqual("[Square] (2) 2/0 - 3", str(sqr_2))

    def test_update_args(self):
        """test update function non-keyword arguments
        """
        sqr = Square(1, 3, 1, 2)

        sqr.update(4, 5)
        self.assertEqual("[Square] (4) 3/1 - 5", str(sqr))

        self.assertEqual(sqr.area(), 25)
        self.assertEqual(sqr.size, 5)
        self.assertEqual(sqr.id, 4)

        # Assert TypeError
        with self.assertRaises(TypeError) as error:
            sqr.update(2, 1.3)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_update_kwargs(self):
        """test update function keyword arguments
        """
        sqr = Square(1, 3, 1, 2)

        sqr.update(size=4, y=5)
        self.assertEqual("[Square] (2) 3/5 - 4", str(sqr))

        self.assertEqual(sqr.area(), 16)
        self.assertEqual(sqr.size, 4)

        # Assert update doesn't assign attributes for invalid keywords
        with self.assertRaises(AttributeError):
            sqr.update(fake_atr=2)
            sqr.fake_atr

    def test_to_dictionary(self):
        sqr = Square(2, 3)
        sqr_dict = sqr.to_dictionary()

        self.assertEqual(sqr_dict["size"], 2)
        self.assertEqual(sqr_dict["x"], 3)
        self.assertEqual(sqr_dict["y"], 0)
