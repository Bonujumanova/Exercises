import string

error_message = [
    "***",
    "Пароль должен начинаться с заглавной буквы",
    "Пароль должен состоять только из латинских букв, цифр и символа нижнего подчёркивания ( _ )",
    "Пароль должен заканчиваться только латинской буквой или цифрой",
    "Минимальная длина пароля — 12 символов, максимальная — 32 символа"
]
print(*error_message, sep="\n", end="\n\n")


def has_digit(password):
    for digit in string.digits:
        if digit in password:
            return True
    print("Пароль должен состоять только из латинских букв, цифр и символа нижнего подчёркивания ( _ )")
    return False


def find_upper_letter(password):
    if password[0] not in string.ascii_uppercase:
        print("Пароль должен начинаться с заглавной буквы")
        return False
    return True


def has_underscore(password):
    if "_" not in password:
        print("Пароль должен содержать символ нижнего подчеркивания")
        return False
    return True


def find_length(password, min_length, max_length):
    if not(min_length <= len(password) <= max_length):
        print("Длина пароля не соответствует требованиям")
        return False
    return True


def check_last_sym(password):
    if password[-1] not in (string.ascii_letters + string.digits):
        print("Пароль должен заканчиваться только латинской буквой или цифрой")
        return False
    return True


def get_password():
    password: str = input("Введите пароль: ")
    return password


def main():

    min_length: int = 12
    max_length: int = 32

    user_password = get_password()
    a = has_digit(user_password)
    b = find_upper_letter(user_password)
    c = find_length(user_password, min_length, max_length)
    d = has_underscore(user_password)
    e = check_last_sym(user_password)


    if all([a, b, c, d, e]):
        print("Пароль принят!")
        with open("valid_passwords.txt", "a", encoding="UTF-8") as f:
            f.write(user_password + "\n")
        return True
    return False


while True:
    result = main()

    if result:
        break
