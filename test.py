import unittest
from main import main, make_few_words


class TestAddCase(unittest.TestCase):
    def test_1(self):
        res = main("продАЖ()", "с")
        self.assertEqual(res, "продАЖ{''}\n")

    def test_2(self):
        res = main("арбитрАЖный()", "с")
        self.assertEqual(res, "продАЖ{''}\nарбитрАЖный{''}\n")

    def test_3(self):
        res = main("продАЖ()", "с")
        self.assertEqual(res, "арбитрАЖный{''}\nпродАЖ{''}\n")

    def test_4(self):
        res = main("пАЧе()", "с")
        self.assertEqual(res, "пАЧе{''}\n")

    def test_5(self):
        res = main("пАтЧ()", "с")
        self.assertEqual(res, "пАЧе{''}\nпАтЧ{''}\n")

    def test_6(self):
        res = main("ЧАд()", "с")
        self.assertEqual(res, "ЧАд{''}\n")

    def test_7(self):
        res = main("тАнЦы()", "с")
        self.assertEqual(res, "тАнЦы{''}\n")

    def test_8(self):
        res = main("абзАЦ()", "с")
        self.assertEqual(res, "тАнЦы{''}\nабзАЦ{''}\n")

    # def test_9(self):
    #     t1, t2 = make_few_words("")

