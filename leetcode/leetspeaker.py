try:
    import pyperclip
    import random
    from pprint import pprint

except ModuleNotFoundError:
    print("Ошибка! Модуль 'pyperclip' не установлен")
else:

    def get_message():
        try:
            user_language: int = int(input(
                "Для выбора русского языка нажмите '1' | To select the English, press '2' "
            ))
            if user_language not in range(1, 3):
                raise ValueError ("Ошибка! / Error")
        except ValueError as er_message:
            print(er_message)
        else:
            system_gret: dict[int, str] = {
                1 : "Для конвертации из русского языка на leet нажмите '1', если наоборот - '2' ",
                2 : "To convert from English to leet, press '1', if the opposite is the case, press '2' "
            }
            print(system_gret[user_language])
            to_leet_or_from = int(input())

            print("Введите ваше сообщение: ")
            message: str = input("> ")
            return user_language, to_leet_or_from, message


    def return_eng_dict():
        eng_char_mapping: dict[str, list] = {
            "a": ["4", "@", "/-\\"],
            "c": ["("],
            "d": ["|)"],
            "e": ["3"],
            "f": ["ph"],
            "h": ["]-[", "|-|"],
            "i": ["1", "!", "|"],
            "k": ["]<"],
            "o": ["0"],
            "s": ["$", "5"],
            "t": ["7", "+"],
            "u": ["|_|"],
            "v": ["\\/"],
        }
        return eng_char_mapping


    def return_rus_dict():
        ru_char_mapping: dict[str, list] = {
            'а': ['4', '@', '/-\\'],
            'г': ['9'],
            'е': ['3', '&', '£', '€', 'ë', '[-|', '=-'],
            'ж': ['>|<', '}|{', ']|['],
            'к': [']<'],
            'л': ['/\\', 'J[', 'J|'],
            'о': ['0'],
            'п': ['|^|', '/7'],
            'р': ['|>'],
            'с': ['(', '[', '¢', '<', '(', '©'],
            'ф': ['<|>', 'qp'],
            'ш': ['III', 'w', 'LL|'],
            'ю': ['|-O'],
            'я': ['9I']
        }
        return ru_char_mapping


    def from_some_lang_to_leetspeak(message, some_char_mapping):
        leetspeak: str = ""
        probability: float = 1
        for char in message:
            if char.lower() in some_char_mapping and random.random() <= probability:
                possible_leet_replacements = some_char_mapping[char.lower()]
                leet_replacement = random.choice(possible_leet_replacements)
                leetspeak = leetspeak + leet_replacement
            else:
                leetspeak = leetspeak + char
        return leetspeak


    #Исправить логику,в some_speak повторения
    def from_leet_to_some_language(message, some_language_char_mapping):
        some_speak: str = ""
        for char in message:
            for key, values in some_language_char_mapping.items():
                if char in values:
                    some_speak += key
                    print(key, end="")
            else:
                some_speak += char
        return some_speak


    def main():
        language, to_leet_or_from, message = get_message()

        if language == 1:
            letters_dict = return_rus_dict()
            if to_leet_or_from == 1:
                ru_to_leet = from_some_lang_to_leetspeak(message, letters_dict)
                print(ru_to_leet)
            else:
                leet_to_some_lang =  from_leet_to_some_language(message, letters_dict)
                print(leet_to_some_lang)
        else:
            letters_dict = return_eng_dict()
            if to_leet_or_from == 1:
                eng_to_leetspeak = from_some_lang_to_leetspeak(message, letters_dict)
                print(eng_to_leetspeak)
            else:
                leet_to_some_lang = from_leet_to_some_language(message, letters_dict)
                print(leet_to_some_lang)

    main()

