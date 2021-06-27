import unittest
from main import main


class TestAddCase(unittest.TestCase):
    def test_1(self):
        res = main("продАЖ(ный)", "с")
        self.assertEqual(res, "продАЖ{'ный'}\n")

    def test_2(self):
        res = main("арбитрАЖный()", "с")
        self.assertEqual(res, "продАЖ{'ный'}\nарбитрАЖный{''}\n")

    def test_3(self):
        res = main("продАЖ(а)", "с")
        self.assertEqual(res, "арбитрАЖный{''}\nпродАЖ{'а', 'ный'}\n")

    def test_4(self):
        res = main()
