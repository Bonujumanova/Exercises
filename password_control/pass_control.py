error_message = [
    "***",
    "Пароль должен начинаться с заглавной буквы",
    "Пароль должен состоять только из латинских букв, цифр и символа нижнего подчёркивания ( _ )",
    "Пароль должен заканчиваться только латинской буквой или цифрой",
    "Минимальная длина пароля — 12 символов, максимальная — 32 символа"
    ]

print(*[message for message in error_message], sep="\n", end="\n\n")
print("Введите пароль: ")

allowed_chars: str = ('_0123456789' + ''.join(chr(letter) for letter in range(65, 91)) +
     ''.join(chr(letter) for letter in range(97, 123)))

letters: str = (
        ''.join(chr(letter) for letter in range(65, 91)) +
        ''.join(chr(letter) for letter in range(97, 123))
        )

digits: str = '0123456789'
symbol: str = '_'
len_flag = False
first_eng_letters_flag = False
symbol_flag = False
digits_flag = False
end_char_flag = False

count_digits: int = 0

while True:
    try:
        user_password: str = input()
        count_char = 0

        if not bool(user_password):
            raise ValueError

        for char in user_password:
            if char not in allowed_chars:
                raise ValueError



    except ValueError:
        print("Для правильного вводв пароля ознакомьтесь с требованиями выше!")

    else:

        for char in user_password:
            if char in digits:
                count_digits += 1
        if count_digits > 0:
            digits_flag = True

        if 12 <= len(user_password) <= 32:
            len_flag = True

        if 65 <= ord(user_password[0]) <= 90:
                first_eng_letters_flag = True

        if user_password[-1] in letters:
            end_char_flag = True
        elif user_password[-1] in digits:
            end_char_flag = True

        if symbol in user_password:
            symbol_flag = True


        if all([len_flag, first_eng_letters_flag, end_char_flag, symbol_flag, digits_flag]):
            print("Пароль принят!")
            with open("valid_passwords.txt", "a", encoding="UTF-8") as f:
                f.write(user_password + "\n")
            break

        else:
            print("Пароль не соответствует требованиям!", end="\n")
            if not len_flag:
                print("Длина пароля не соответствует требованиям")
            if not end_char_flag:
                print("Пароль должен заканчиваться только латинской буквой или цифрой")
            if not first_eng_letters_flag:
                print("Пароль должен начинаться с заглавной буквы")
            if not symbol:
                print("Пароль должен содержать символ нижнего подчеркивания")
            if not digits_flag:
                print("Пароль должен содержать цыфру(ы)")
            break


# №2
# while True:
#     try:
#         user_password: str = input()
#         count_char = 0
#         if 12 <= len(user_password) <= 32 and 65 <= ord(user_password[0]) <= 90 \
#                 and user_password[-1] in allowed_chars[1:]:
#             for char in user_password:
#                 if char in allowed_chars:
#                     count_char += 1
#
#             if (count_char == len(user_password) and "_" in user_password):
#                 print("Пароль принят!")
#                 with open("valid_passwords.txt", "a", encoding="UTF-8") as f:
#                     f.write(user_password + "\n")
#                 break
#
#             else:
#                 print("Пароль не соответствует требованиям!")
#                 break
#         else:
#             raise ValueError
#
#     except ValueError:
#         print("Для правильного вводв пароля ознакомьтесь с требованиями выше!")
