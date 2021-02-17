import unittest
from models.base_model import BaseModel

class TestClass(unittest.TestCase):


    def test_one_instance(self):
        b1 = BaseModel()
        b1.name = "Holberton"
        self.assertEqual(b1.name, "Holberton")

    def test_an_other_value(self):
        b1 = BaseModel()
        b1.my_number = 23
        self.assertEqual(b1.my_number, 23)
