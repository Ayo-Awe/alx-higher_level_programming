#!/usr/bin/python3
"""Base Test Module
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBaseClass(unittest.TestCase):
    """TestBaseClass
    """

    def tearDown(self) -> None:
        """tearDown function

        Removes any json files created during the course of a test
        """
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_id(self):
        """test_id function
        Tests that the logic for id works as
        expected i.e initialises object with id if specified
        or defaults to number of instances with default ids
        """
        # Create three instances of the base class
        base_1 = Base(1)
        base_2 = Base(8)
        base_3 = Base(2)

        # Assert their id values
        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 8)
        self.assertEqual(base_3.id, 2)

    def test_to_json_string(self):
        """test_to_json_string function
        Tests that the logic for to_json_string works as
        expected
        """

        rect = Rectangle(3, 6, 0, 0, 3)
        sqr = Square(3, 0, 0, 4)

        rect_dictionary = rect.to_dictionary()
        sqr_dictionary = sqr.to_dictionary()

        json = Base.to_json_string([rect_dictionary, sqr_dictionary])

        self.assertEqual(
            json, '[{"id": 3, "width": 3, "height": 6, "x": 0, "y": 0}, {"id": 4, "size": 3, "x": 0, "y": 0}]')

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_save_to_file(self):
        rect = Rectangle(2, 3)
        square = Square(2)

        Rectangle.save_to_file([rect])
        Square.save_to_file([square])

        # Test save to file for Rectangle
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            content = file.read()
            self.assertEqual(content, Base.to_json_string(
                [rect.to_dictionary()]))
            file.close()

        # Test save to file for square
        with open("Square.json", "r", encoding="utf-8") as file:
            content = file.read()
            self.assertEqual(content, Base.to_json_string(
                [square.to_dictionary()]))
            file.close()

        square.update(x=3)
        Square.save_to_file([square])

        # Test file overwrite
        with open("Square.json", "r", encoding="utf-8") as file:
            content = file.read()
            self.assertEqual(content, Base.to_json_string(
                [square.to_dictionary()]))
            file.close()

        # Test save to file with none
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            content = file.read()
            self.assertEqual(content, "[]")
            file.close()

    def test_create(self):
        rect = Rectangle(2, 3, 1, 5, 1)
        square = Square(2, 3, 1, 5)

        # Test create with instance from dictionary
        rect_dict = rect.to_dictionary()
        square_dict = square.to_dictionary()

        rect_1 = Rectangle.create(**rect_dict)
        square_1 = Square.create(**square_dict)

        self.assertEqual(rect_1.area(), rect.area())
        self.assertEqual(square_1.area(), square.area())

        self.assertEqual(rect_1.to_dictionary(), rect.to_dictionary())
        self.assertEqual(square_1.to_dictionary(), square.to_dictionary())

        self.assertNotEqual(id(rect), id(rect_1))
        self.assertNotEqual(id(square), id(square_1))

    def test_load_from_file(self):
        # @TODO
        # Test file doesn't exists
        rect_instances = Rectangle.load_from_file()
        self.assertEqual(rect_instances, [])

        # Test save to file then load from file
        rect = Rectangle(2, 3)
        square = Square(2)

        Rectangle.save_to_file([rect])
        Square.save_to_file([square])

        square_instances = Square.load_from_file()
        rect_instances = Square.load_from_file()

        self.assertTrue(any(isinstance(square, Square)
                        for square in square_instances))

        self.assertEqual(len(square_instances), 1)

        self.assertTrue(any(isinstance(rectangle, Rectangle)
                        for rectangle in rect_instances))

        self.assertEqual(len(rect_instances), 1)
