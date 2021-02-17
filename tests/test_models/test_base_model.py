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

    def test_verify_id(self):
        b1 = BaseModel()
        self.assertTrue(b1.id)

    def test_verify_create_date(self):
        b1 = BaseModel()
        self.assertTrue(b1.created_at)

    def test_verify_create_date(self):
        b1 = BaseModel()
        self.assertTrue(b1.updated_at)

