import unittest
from models.base_model import BaseModel

class TestClass(unittest.TestCase):


    def test_one_instance(self):
        b1 = BaseModel()
        b1.name = "Holberton"
        self.assertTrue(b1.name)

    def test_an_other_value(self):
        b1 = BaseModel()
        b1.my_number = 23
        self.assertTrue(b1.my_number)

    def test_verify_id(self):
        b1 = BaseModel()
        self.assertTrue(b1.id)

    def test_verify_create_date(self):
        b1 = BaseModel()
        self.assertTrue(b1.created_at)

    def test_verify_updated_date(self):
        b1 = BaseModel()
        self.assertTrue(b1.updated_at)

    def test_verify_class_exist(self):
        b1 = BaseModel()
        self.assertTrue(b1.__class__)

    def test_print(self):
        b1 = BaseModel()
        self.assertIsNotNone(b1.__str__)

    def test_save(self):
        b1 = BaseModel()
        self.assertIsNotNone(b1.save)

    def test_to_dict(self):
        b1 = BaseModel()
        self.assertIsNotNone(b1.to_dict)
