import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_get_full_name(self):
        e = Employee("Vera", "Schmidt", 0, None)
        self.assertEqual(e.get_full_name(), "Vera Schmidt")

