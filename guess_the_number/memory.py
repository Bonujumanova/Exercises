import random

hidden_number = random.randint(1, 100)

number_of_attempts: int = 10
i = 1

while i < 11:
    try:
        user_num: int = int(input("Введите число: "))
    except ValueError:
         print("Введите числовое значение!")
    else:
        if user_num < hidden_number:
            print("Загаданное число больше!")
        elif user_num > hidden_number:
            print("Загаданное число меньше")
        else:
            print(f"Поздравляем! Вы угадали число за {i} попыток!")
            break
        i += 1

else:
    print(f"К сожалению, вы не угадали число. Загаданное число было {hidden_number}.")
