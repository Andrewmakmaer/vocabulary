import sqlite3 as sq

capital_vowel_letters = ("А", "Е", "Ё", "И", "О", "У", "Э", "Ы", "Ю", "Я")
capital_consonant_letters = ("Ш", "Ж", "Ч", "ТЩ", "Ц", "ТС", "С", "З", "Р")
set_beech2 = ("А", "О", "У", "И", "Э")
set_beech1 = ("А(Я)", "О(Ё)", "У(Ю)", "Ы(И)", "Э(Е)")


def choice_vow_letter_for_set_1(letter):
    if letter == "А" or "Я":
        return "А(Я)"
    elif letter == "О" or "Ё":
        return "О(Ё)"
    elif letter == "У" or "Ю":
        return "У(Ю)"
    elif letter == "Ы" or "И":
        return "Ы(И)"
    elif letter == "Э" or "Е":
        return "Э(Е)"


def make_few_words(words):
    root_word, end_word = words.split('(')
    end_word = end_word.replace(')', '')
    list_of_end = end_word.split('/')
    return root_word, set(list_of_end)


def choice_base_letter(letter):
    if letter == "Ш" or letter == "Ж":
        return 'Ш(Ж)'
    elif letter == "Ч" or letter == "ТЩ":
        return 'Ч(ТЩ)'
    elif letter == "Ц" or letter == "ТС":
        return 'Ц(ТС)'
    elif letter == "С" or letter == "З":
        return 'С(З)'
    if letter == "Р":
        return 'Р'


def check_capital_less(root):
    vow_les = ""
    con_les = ""
    for item in capital_vowel_letters:
        if item in root:
            vow_les = item
            break
    for item in capital_consonant_letters:
        if item in root:
            con_les = item
            break

    if root.find(vow_les) < root.find(con_les):
        return vow_les, con_les, True
    else:
        return vow_les, con_les, False


class Word:
    def __init__(self, words_and_end, part_of_speech):
        self.words_and_end = words_and_end
        self.vow_less, self.con_less, self.vow_bef = check_capital_less(words_and_end[0])
        self.part_of_speech = part_of_speech


# test = Word(make_few_words("ШАр(ик/ундул/оёбы)"), "s")
# print(test.con_less, test.vow_less, test.vow_bef, test.words_and_end, test.part_of_speech)


def check_separation_letters(object_Word):
    if abs(object_Word.words_and_end[0].find(object_Word.con_less)
           - object_Word.words_and_end[0].find(object_Word.vow_less)) > 1:
        return True
    else:
        return False


with sq.connect("main_base.db") as con:
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS vocabulary 
                         (word TEXT,
                         end TEXT,
                         con_less TEXT,
                         vow_less TEXT,
                         vow_bef INTEGER,
                         part_of_speech TEXT)""")

    input_list = [item for item in input().split()]

    if input_list[0] == "show":
        for row in cursor.execute("SELECT * FROM vocabulary"):
            print(row)

        exit()

    object_Word = Word(make_few_words(input_list[0]), input_list[1])

    if choice_base_letter(object_Word.con_less) == "Ш(Ж)":
        if check_separation_letters(object_Word):
            if object_Word.vow_less in set_beech2 and not object_Word.vow_bef:
                cursor.execute("INSERT INTO vocabulary VALUES(?, ?, ?, ?, ?, ?)", [str(object_Word.words_and_end[0]),
                                                                                   str(object_Word.words_and_end[1]),
                                                                                   str(object_Word.con_less),
                                                                                   str(object_Word.vow_less),
                                                                                   int(object_Word.vow_bef),
                                                                                   str(object_Word.part_of_speech)])
        else:
            if object_Word.vow_bef:
                cursor.execute("INSERT INTO vocabulary VALUES(?, ?, ?, ?, ?, ?)", [str(object_Word.words_and_end[0]),
                                                                                   str(object_Word.words_and_end[1]),
                                                                                   str(object_Word.con_less),
                                                                                   choice_vow_letter_for_set_1(
                                                                                       str(object_Word.vow_less)),
                                                                                   int(object_Word.vow_bef),
                                                                                   str(object_Word.part_of_speech)])
            else:
                cursor.execute("INSERT INTO vocabulary VALUES(?, ?, ?, ?, ?, ?)", [str(object_Word.words_and_end[0]),
                                                                                   str(object_Word.words_and_end[1]),
                                                                                   str(object_Word.con_less),
                                                                                   str(object_Word.vow_less),
                                                                                   int(object_Word.vow_bef),
                                                                                   str(object_Word.part_of_speech)])

    if choice_base_letter(object_Word.con_less) == "Ч(ТЩ)":
        if check_separation_letters(object_Word):
            pass
        else:
            pass
