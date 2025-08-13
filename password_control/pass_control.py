import string

error_message = [
    "***",
    "Пароль должен начинаться с заглавной буквы",
    "Пароль должен состоять только из латинских букв, цифр и символа нижнего подчёркивания ( _ )",
    "Пароль должен заканчиваться только латинской буквой или цифрой",
    "Минимальная длина пароля — 12 символов, максимальная — 32 символа"
]

print(*error_message, sep="\n", end="\n\n")
underscore: str = "_"
letters: str = string.ascii_letters
allowed_chars: str = letters + string.digits + underscore

count_digits: int = 0
errors: list[str] = []
while True:
    user_password: str = input("Введите пароль: ")

    for digit in string.digits:
        if digit in user_password:
            break
    else:
        print("Пароль должен содержать цыфру(ы)")
        continue

    # TODO: Магические числа вынести в константы
    if not (12 <= len(user_password) <= 32):
        errors.append("Длина пароля не соответствует требованиям")

    if user_password[0] not in string.ascii_uppercase:
        print("Пароль должен начинаться с заглавной буквы")
        continue

    if user_password[-1] not in (letters + string.digits):
        # if not user_password.endswith(tuple(letters + string.digits)):
        print("Пароль должен заканчиваться только латинской буквой или цифрой")
        continue

    if underscore not in user_password:
        print("Пароль должен содержать символ нижнего подчеркивания")

    if not errors:
        print("Пароль принят!")
        with open("valid_passwords.txt", "a", encoding="UTF-8") as f:
            f.write(user_password + "\n")
        break
    else:
        print("Пароль не соответствует требованиям!", end="\n")
        print("\n".join(errors))
