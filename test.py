import unittest
from main import main


class TestAddCase(unittest.TestCase):
    def test_1(self):
        res = main("продАЖ(ный)", "с")
        self.assertEqual(res, "продАЖ{'ный'}")
