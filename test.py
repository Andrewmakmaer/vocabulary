import unittest
from main import main, make_few_words


class TestAddCase(unittest.TestCase):
    def test_0(self):
        res = main("свЯЗь()", "с")
        self.assertEqual(res, "свЯЗь{''}\n")

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

    def test_9(self):
        res = main("пАСека()", "с")
        self.assertEqual(res, "свЯЗь{''}\nпАСека{''}\n")

    def test_10(self):
        res = main("небеСА()", "с")
        self.assertEqual(res, "небеСА{''}\n")

    def test_11(self):
        res = main("тРАвы()", "с")
        self.assertEqual(res, "тРАвы{''}\n")

    def test_12(self):
        res = main("обРЯд()", "с")
        self.assertEqual(res, "обРЯд{''}\n")

    def test_13(self):
        res = main("лОР()", "с")
        self.assertEqual(res, "лОР{''}\n")

    # def test_some(self):
    #     t1, t2 = make_few_words("")

