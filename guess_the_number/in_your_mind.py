from random import randint
from math import log

print("Загадайте число в уме, а программа попробует угадать!")
print()

while True:
    try:
        number_1:int = int(input("Введите начало диапазона загаданного числа"))
        number_2: int = int(input("Введите конец диапазона загаданного числа"))

        if number_1 == number_2:
            raise ValueError("Числа не должны быть равны!")

    except ValueError:
        print("Введите целое натуральное число!!!")

    else:
        start_num_1, end_num_1 = sorted([number_1, number_2])
        break


nums = range(start_num_1, end_num_1)
number_of_attempts: int = int(log(len(nums), 2)) + 1

i: int = 1

program_answer = randint(start_num_1, end_num_1)
print(program_answer)

while i != 11:

    try:
        user_input: str = input("Загаданное число ")
        if program_answer == start_num or program_answer == end_num:
            raise ValueError()


    except:

        print("Играйте по правилам!")
    else:
        print(program_answer)

        if user_input == "больше":
            start_num = program_answer
            program_answer = randint(start_num, end_num)
        elif user_input == "меньше":
            end_num = program_answer
            program_answer = randint(start_num, end_num)
        elif user_input == "угадал":
            print(f"Я угадал ! Загаданное число {program_answer}. Количество попыток: {i}")

        i += 1

