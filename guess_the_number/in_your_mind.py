from math import log

print("Загадайте число в уме, а программа попробует угадать!\n")
start_num_1: int = 0
end_num_1: int = 0
min_num: int = 0
max_num: int = 0
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
    min_num: int = start
    max_num: int = end
    break

nums: range = range(start_num_1, end_num_1)
answers: tuple[str, str, str] = ("больше", "меньше", "угадал")
number_of_attempts: int = int(log(len(nums), 2)) + 1
i: int = 0
flag: bool = True
continue_flag: bool = True
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

    if continue_flag:
        if user_input == "больше":
            start_num_1 = program_answer_1 + 1

        elif user_input == "меньше":
             end_num_1 = program_answer_1 - 1

    if  start_num_1 > end_num_1:
        continue_flag =  False
        print("Ошибка! Похоже, вы дали противоречивые ответы.")
        break
