import sqlite3 as sq

capital_vowel_letters = ("А", "Е", "Ё", "И", "О", "У", "Э", "Ы", "Ю", "Я")
capital_consonant_letters = ("Ш", "Ж", "Ч", "ТЩ", "Ц", "ТС", "С", "З", "Р")
set_beech1 = ("А(Я)", "О(Ё)", "У(Ю)", "Ы(И)", "Э(Е)")
set_beech2 = ("А", "О", "У", "И", "Э")
set_beech3 = ("А", "О", "У", "Ы", "Э")
set_beech4 = ("Я", "Ё", "Ю", "И", "Е")


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
        self.words_and_end = list(words_and_end)
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


def main(input_1, input_2=None):
    with sq.connect("main_base.db") as con:
        cursor = con.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS vocabulary 
                             (type TEXT,
                             word TEXT,
                             end TEXT,
                             con_less TEXT,
                             vow_less TEXT,
                             vow_bef INTEGER,
                             part_of_speech TEXT)""")

        if input_1 == "show":
            for row in cursor.execute("SELECT * FROM vocabulary"):
                print(row)

            exit()

        object_Word = Word(make_few_words(input_1), input_2)

        def print_set_words(type, vow_less):
            result = ""
            for sim_word in cursor.execute("""SELECT word, end FROM vocabulary WHERE type = ? AND
                            vow_less = ? AND vow_bef = ? AND part_of_speech = ?""", [type,
                                                                                     vow_less,
                                                                                     int(object_Word.vow_bef),
                                                                                     str(object_Word.part_of_speech)]):
                result = result + (sim_word[0] + sim_word[1]) + "\n"

            return result

        def insert_in_db(type, vow_type):
            overwrite_entry()
            cursor.execute("INSERT INTO vocabulary VALUES(?, ?, ?, ?, ?, ?, ?)", [type,
                                                                                  str(object_Word.words_and_end[0]),
                                                                                  str(object_Word.words_and_end[1]),
                                                                                  str(object_Word.con_less),
                                                                                  vow_type,
                                                                                  int(object_Word.vow_bef),
                                                                                  str(object_Word.part_of_speech)])
            return print_set_words(type, vow_type)

        def overwrite_entry():
            for item in cursor.execute("SELECT end FROM vocabulary WHERE word = ?",
                                       [object_Word.words_and_end[0]]):
                old_end = set(item[0][1:-1].replace(",", "").replace("'", "").split())
                object_Word.words_and_end[1] = object_Word.words_and_end[1].union(old_end)
                cursor.execute("DELETE FROM vocabulary WHERE word = ?", [object_Word.words_and_end[0]])

        if choice_base_letter(object_Word.con_less) == "Ш(Ж)":
            if check_separation_letters(object_Word):
                if object_Word.vow_less in set_beech2 and not object_Word.vow_bef:
                    return insert_in_db("Ш(Ж)'", str(object_Word.vow_less))
            else:
                if object_Word.vow_bef and choice_vow_letter_for_set_1(str(object_Word.vow_less)) in set_beech1:
                    return insert_in_db("Ш(Ж)", choice_vow_letter_for_set_1(str(object_Word.vow_less)))
                elif str(object_Word.vow_less) in set_beech2:
                    return insert_in_db("Ш(Ж)", str(object_Word.vow_less))

        elif choice_base_letter(object_Word.con_less) == "Ч(ТЩ)":
            if not object_Word.vow_bef and check_separation_letters(object_Word):
                if object_Word.vow_less in set_beech4:
                    return insert_in_db("Ч'", str(object_Word.vow_less))
            else:
                if object_Word.vow_bef and choice_vow_letter_for_set_1(str(object_Word.vow_less)) in set_beech1:
                    return insert_in_db("Ч(ТЩ)", choice_vow_letter_for_set_1(str(object_Word.vow_less)))
                elif str(object_Word.vow_less) in set_beech3:
                    return insert_in_db("Ч(ТЩ)", str(object_Word.vow_less))

        elif choice_base_letter(object_Word.con_less) == "С(З)":
            if object_Word.vow_bef and choice_vow_letter_for_set_1(object_Word.vow_less) in set_beech1:
                return insert_in_db("'С(ТС)", choice_vow_letter_for_set_1(object_Word.vow_less))
            elif not object_Word.vow_bef and object_Word.vow_less in set_beech3:
                return insert_in_db("С(ТС)'", object_Word.vow_less)
            elif object_Word.vow_less in set_beech4:
                return insert_in_db("С(ТС)Ь", object_Word.vow_less)

        elif choice_base_letter(object_Word.con_less) == "Ц(ТС)":
            if object_Word.vow_bef:
                return insert_in_db("Ц(ТС)", choice_vow_letter_for_set_1(object_Word.vow_less))
            elif not object_Word.vow_bef:
                return insert_in_db("Ц(ТС)", str(object_Word.vow_less))

        elif choice_base_letter(object_Word.con_less) == "Р":
            if object_Word.vow_bef:
                return insert_in_db("Р", object_Word.vow_less)
            elif object_Word.vow_less in set_beech3:
                return insert_in_db("Р", object_Word.vow_less)
            elif object_Word.vow_less in set_beech4:
                return insert_in_db("Р(ь)", object_Word.vow_less)


if __name__ == "__main__":
    while True:
        input_list = [item for item in input().split()]
        print((main(input_list[0], input_list[1]))[:-1])
