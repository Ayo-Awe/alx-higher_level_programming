"""Base Test Module
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """TestBaseClass
    """

    def test_id(self):
        """test_id function
        Tests that the logic for id works as
        expected i.e initialises object with id if specified
        or defaults to number of instances with default ids
        """
        # Create three instances of the base class
        base_1 = Base()
        base_2 = Base(8)
        base_3 = Base()

        # Assert their id values
        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 8)
        self.assertEqual(base_3.id, 2)
