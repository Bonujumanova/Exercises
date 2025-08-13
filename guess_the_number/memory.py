import random

hidden_number: int = random.randint(1, 100)

number_of_attempts: int = 10
i: int = 1
while i < number_of_attempts:
    try:
        user_num: int = int(input("Введите число: "))
    except ValueError:
        print("Введите числовое значение!")
    else:
        if user_num == hidden_number:
            print(f"Поздравляем! Вы угадали число за {i} попыток!")
            break

        if user_num < hidden_number:
            print("Загаданное число больше!")
        elif user_num > hidden_number:
            print("Загаданное число меньше")

        i += 1
else:
    print(
        "К сожалению, вы не угадали число. "
        f"Загаданное число было {hidden_number}."
    )
