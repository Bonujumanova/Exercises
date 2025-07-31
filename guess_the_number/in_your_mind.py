from random import randint
from math import log

print("Загадайте число в уме, а программа попробует угадать!")
print()

while True:
    try:
        number_1:int = int(input("Введите начало диапазона загаданного числа"))
        number_2: int = int(input("Введите конец диапазона загаданного числа"))

    except ValueError:
        print("Введите целое натуральное число!!!")

    else:
        if number_1 == number_2:
            print("Числа не должны быть равны!")

        else:
            start_num_1, end_num_1 = min(number_1, number_2), max(number_1, number_2)
            break


nums = range(start_num_1, end_num_1)
number_of_attempts: int = int(log(len(nums), 2)) + 1

i = 0

while i != 11:
    program_answer_1 = (start_num_1 + end_num_1) // 2
    print(program_answer_1)
    user_input: str = input()
    if user_input == "больше":
        start_num_1 = program_answer_1 + 1
    elif user_input == "меньше":
        end_num_1 = program_answer_1 - 1
    elif user_input =="угадал":
        print(f"Я угадал! Загаданное число {program_answer_1}. Количество попыток: {i}")
        break
    if program_answer_1 <= number_1 or program_answer_1 >= number_2:
        print("Ошибка! Похоже, вы дали противоречивые ответы.")
        break

    i += 1
