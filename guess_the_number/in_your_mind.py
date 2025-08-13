from math import log

print("Загадайте число в уме, а программа попробует угадать!\n")
while True:
    start, end = input(
        "Введите начало и конец диапазона загаданного числа > "
    ).split()

    if not (start.isdigit() and end.isdigit()):
        print("Введите целое натуральное число!!!")
        continue

    if start == end:
        print("Числа не должны быть равны!")
        continue

    start, end = int(start), int(end)
    start_num_1, end_num_1 = min(start, end), max(start, end)
    break

nums: range = range(start_num_1, end_num_1)
answers: tuple[str, str, str] = ("больше", "меньше", "угадал")
number_of_attempts: int = int(log(len(nums), 2)) + 1
i: int = 0
flag: bool = True
while i < number_of_attempts:
    program_answer_1 = (start_num_1 + end_num_1) // 2
    if flag:
        print(program_answer_1)
        i += 1

    user_input: str = input()
    if user_input not in answers:
        print(f"Возможные варианты ответов: {answers}")
        flag = False
        continue

    flag = True
    if user_input == "угадал":
        print(
            f"Я угадал! Загаданное число {program_answer_1}. "
            f"Количество попыток: {i}"
        )
        break

    if user_input == "больше":
        start_num_1 = program_answer_1 + 1
    elif user_input == "меньше":
        end_num_1 = program_answer_1 - 1
else:
    # if program_answer_1 not in nums:
    print("Ошибка! Похоже, вы дали противоречивые ответы.")
    # break

# TODO: После вывода 1, следующим должен быть ответ:
#  'Ошибка! Похоже, вы дали противоречивые ответы.'
"""
Введите начало и конец диапазона загаданного числа > 1 30
15
меньше
7
меньше
3
меньше
1
меньше
0
меньше
Ошибка! Похоже, вы дали противоречивые ответы.
"""
