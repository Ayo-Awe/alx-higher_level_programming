#!/usr/bin/python3
"""Base Test Module
"""
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """TestRectangleClass
    """

    def test_create_rectangle(self):
        """test_create_rectangle function
        Tests successful creation of rectangle instance
        """
        # Create new instance of rectangle
        rect_1 = Rectangle(10, 20, 3, 2)
        rect_2 = Rectangle(10, 20, 3, 2, 12)

        # Rectangle attributes are set accurately
        self.assertEqual(rect_1.width, 10)
        self.assertEqual(rect_1.height, 20)
        self.assertEqual(rect_1.x, 3)
        self.assertEqual(rect_1.y, 2)

        self.assertEqual(rect_2.id, 12)

    def test_width_type(self):
        """test_width_type function
        """
        # Create new instance of rectangle
        rect = Rectangle(10, 20, 3, 2)

        # Assert TypeError
        with self.assertRaises(TypeError) as error:
            rect.width = "hello"

        self.assertEqual("width must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            rect.width = 10.2

        self.assertEqual("width must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            rect.width = None

        self.assertEqual("width must be an integer", str(error.exception))

    def test_width_value(self):
        """test_width_value function
        """
        # Create new instance of rectangle
        rect = Rectangle(10, 20, 3, 2)
        self.assertEqual(rect.width, 10)

        rect.width = 30
        self.assertEqual(rect.width, 30)

        # Assert ValueError
        with self.assertRaises(ValueError) as error:
            rect.width = -2

        self.assertEqual("width must be > 0", str(error.exception))

        with self.assertRaises(ValueError) as error:
            rect.width = 0

        self.assertEqual("width must be > 0", str(error.exception))

    def test_height_type(self):
        """test_height_type function
        """
        # Create new instance of rectangle
        rect = Rectangle(10, 20, 3, 2)

        # Assert TypeError
        with self.assertRaises(TypeError) as error:
            rect.height = "hello"

        self.assertEqual("height must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            rect.height = -0.2

        self.assertEqual("height must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            rect.height = None

        self.assertEqual("height must be an integer", str(error.exception))

    def test_height_value(self):
        """test_height_value function
        """
        # Create new instance of rectangle
        rect = Rectangle(10, 20, 3, 2)
        self.assertEqual(rect.height, 20)

        rect.height = 15
        self.assertEqual(rect.height, 15)

        # Assert ValueError
        with self.assertRaises(ValueError) as error:
            rect.height = -2

        self.assertEqual("height must be > 0", str(error.exception))

        with self.assertRaises(ValueError) as error:
            rect.height = 0

        self.assertEqual("height must be > 0", str(error.exception))

    def test_x_type(self):
        """test_x_type function
        """
        # Create new instance of rectangle
        rect = Rectangle(10, 20, 3, 2)

        # Assert TypeError
        with self.assertRaises(TypeError) as error:
            rect.x = "hello"

        self.assertEqual("x must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            rect.x = -0.2

        self.assertEqual("x must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            rect.x = None

        self.assertEqual("x must be an integer", str(error.exception))

    def test_x_value(self):
        """test_x_value function
        """
        # Create new instance of rectangle
        rect = Rectangle(10, 20, 3, 2)
        self.assertEqual(rect.x, 3)

        rect.x = 10
        self.assertEqual(rect.x, 10)

        rect.x = 0
        self.assertEqual(rect.x, 0)

        # Assert ValueError
        with self.assertRaises(ValueError) as error:
            rect.x = -2

        self.assertEqual("x must be >= 0", str(error.exception))

        with self.assertRaises(ValueError) as error:
            rect.x = -12

        self.assertEqual("x must be >= 0", str(error.exception))

    def test_y_type(self):
        """test_y_type function
        """
        # Create new instance of rectangle
        rect = Rectangle(10, 20, 3, 2)

        # Assert TypeError
        with self.assertRaises(TypeError) as error:
            rect.y = "hello"
        self.assertEqual("y must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            rect.y = -0.2
        self.assertEqual("y must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            rect.y = None
        self.assertEqual("y must be an integer", str(error.exception))

    def test_y_value(self):
        """test_y_value function
        """
        # Create new instance of rectangle
        rect = Rectangle(10, 20, 3, 2)
        self.assertEqual(rect.y, 2)

        rect.y = 10
        self.assertEqual(rect.y, 10)

        rect.y = 0
        self.assertEqual(rect.y, 0)

        # Assert ValueError
        with self.assertRaises(ValueError) as error:
            rect.y = -2

        self.assertEqual("y must be >= 0", str(error.exception))

        with self.assertRaises(ValueError) as error:
            rect.y = -12

        self.assertEqual("y must be >= 0", str(error.exception))

    def test_area(self):
        """test_area
        Tests the public instance method, area
        """

        rect_1 = Rectangle(1, 3, 0, 2, 2)
        rect_2 = Rectangle(3, 13)
        rect_3 = Rectangle(10, 5)

        self.assertEqual(rect_1.area(), 3)
        self.assertEqual(rect_2.area(), 39)
        self.assertEqual(rect_3.area(), 50)

    @patch("builtins.print")
    def test_display(self, mock_print):
        """test_display
        Tests the display instance method
        """

        rect_1 = Rectangle(1, 3)
        rect_2 = Rectangle(3, 2, 0, 6, 2)

        # self.assert

        rect_1.display()
        mock_print.assert_called_with("#\n#\n#\n", end="")

        rect_2.display()
        mock_print.assert_called_with("\n\n\n\n\n\n###\n###\n", end="")

    def test_string_representation(self):
        """test_string_representation function
        Tests the __str__ function
        """

        rect_1 = Rectangle(1, 3, 1, 2, 12)
        rect_2 = Rectangle(3, 2, 0, 6, 2)

        self.assertEqual("[Rectangle] (12) 1/2 - 1/3", str(rect_1))
        self.assertEqual("[Rectangle] (2) 0/6 - 3/2", str(rect_2))

    def test_update_args(self):
        """test update function non-keyword arguments
        """
        rect_1 = Rectangle(1, 3, 1, 2, 12)

        rect_1.update(4, 5)
        self.assertEqual("[Rectangle] (4) 1/2 - 5/3", str(rect_1))

        self.assertEqual(rect_1.area(), 15)
        self.assertEqual(rect_1.width, 5)
        self.assertEqual(rect_1.id, 4)

        rect_1.update(5, 7, 10, 2, 6)
        self.assertEqual("[Rectangle] (5) 2/6 - 7/10", str(rect_1))
        self.assertEqual(rect_1.height, 10)
        self.assertEqual(rect_1.y, 6)
        self.assertEqual(rect_1.x, 2)

        # Assert TypeError
        with self.assertRaises(TypeError) as error:
            rect_1.update(2, 1.3)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_update_kwargs(self):
        """test update function keyword arguments
        """
        rect_1 = Rectangle(1, 3, 1, 2, 12)

        rect_1.update(width=4, y=5)
        self.assertEqual("[Rectangle] (12) 1/5 - 4/3", str(rect_1))

        self.assertEqual(rect_1.area(), 12)
        self.assertEqual(rect_1.width, 4)

        rect_1.update(5, 7, y=9, width=12)
        self.assertEqual("[Rectangle] (5) 1/5 - 7/3", str(rect_1))
        self.assertEqual(rect_1.width, 7)
        self.assertEqual(rect_1.y, 5)

        # Assert update doesn't assign attributes for invalid keywords
        with self.assertRaises(AttributeError):
            rect_1.update(fake_atr=2)
            rect_1.fake_atr

    def test_to_dictionary(self):
        rect = Rectangle(2, 3)
        rect_dict = rect.to_dictionary()

        self.assertEqual(rect_dict["width"], 2)
        self.assertEqual(rect_dict["height"], 3)
        self.assertEqual(rect_dict["x"], 0)
        self.assertEqual(rect_dict["y"], 0)
