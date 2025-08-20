import string

error_message = [
    "***",
    "Пароль должен начинаться с заглавной буквы",
    "Пароль должен состоять только из латинских букв, цифр и символа нижнего подчёркивания ( _ )",
    "Пароль должен заканчиваться только латинской буквой или цифрой",
    "Минимальная длина пароля — 12 символов, максимальная — 32 символа"
]

print(*error_message, sep="\n", end="\n\n")

min_length: int = 12
max_length: int = 32
underscore: str = "_"
letters: str = string.ascii_letters


def find_digit(password):
    for digit in string.digits:
        if digit in user_password:
            return True
    return "Пароль должен состоять только из латинских букв, цифр и символа нижнего подчёркивания ( _ )"


def find_upper_letter(password):
    if user_password[0] not in string.ascii_uppercase:
        return "Пароль должен начинаться с заглавной буквы"
    return True


def find_underscore(password):
    if underscore not in user_password:
        return "Пароль должен содержать символ нижнего подчеркивания"
    return True


def find_length(password):
    if not(min_length <= len(user_password) <= max_length):
        return "Длина пароля не соответствует требованиям"
    return True


def check_last_sym(password):
    if password[-1] not in (letters + string.digits):
        return "Пароль должен заканчиваться только латинской буквой или цифрой"
    return True


def get_password():
    password: str = input("Введите пароль: ")
    return password


def main():
    global user_password

    user_password = get_password()
    a = find_digit(user_password)
    b = find_upper_letter(user_password)
    c = find_length(user_password)
    d = find_underscore(user_password)
    e = check_last_sym(user_password)

    if a == b == c == d == e:
        print("Пароль принят!")
        with open("valid_passwords.txt", "a", encoding="UTF-8") as f:
            f.write(user_password + "\n")
    else:
        for result in [a, b, c, d, e]:
            if result != True:
                print(result)


        main()


main()
