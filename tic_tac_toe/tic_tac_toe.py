from colorama import init, Fore, Back, Style
init()


data: list[list[int | str]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for col in range(len(data)):
    for row in range(len(data[col])):
        if row != 2:
            print(data[col][row], "|", end=" ")
        else:
            print(data[col][row])
    print("-----------")



def show_table(char: str, player_choice: int) -> list:
    # if char == "O":
    #     color = Fore.YELLOW
    # else:
    #     color = Fore.GREEN
    for col in range(len(data)):
        for row in range(len(data[col])):
            if data[col][row] == player_choice:
                data[col][row] = char
            if row != 2:
                print(data[col][row], "|", end=" ")
            else:
                print(data[col][row])
        if col != 2:
            print("----------")

    return data


def check_winner(changed_data: list[list]) -> bool:
    players: dict = {"X": "player_1_name", "O": "player_2_name"}

    for col in range(len(changed_data)):
        if all(changed_data[col][0] == changed_data[col][row] for row in range(len(changed_data[col]))):
            print(f"Вы победили {players.get(changed_data[col][0])}")
            return True
        for row in range(col, col + 1):
            if changed_data[0][row] ==  changed_data[1][row] == changed_data[2][row]:
                print(f"Победил игрок: {players.get(changed_data[col][row])}, '2'")
                return True

        if changed_data[col][0] == changed_data[col][1] == changed_data[col][2]:
            print(f"Победил игрок: {players.get(changed_data[col][1])} '3'")
            return True
        elif changed_data[col][2] == changed_data[col][1] == changed_data[col][0]:
            print(f"Победил игрок: {players.get(changed_data[col][1])} '4'")
            return True

    if all(all((str(j).isalpha() for j in i)) for i in data):
        print("Победителя нет! Постарайтесь выиграть в следующий раз!!!")
        return True
    return False



def get_players_input(first: bool, second: bool, entered_numbers, players_name):

    symbol: str = ""
    player: int = 0

    if second:
        while True:
            try:
                player: int = int(input(f"Ходит игрок 1 {players_name["X"]}: "))
                if 1 <= player <= 9 and player not in entered_numbers:
                    second = False
                    first = True
                    symbol = "X"
                    entered_numbers.append(player)
                    break
                elif player in entered_numbers:
                    print("Это окно уже занято, выберите другое!")
                else:
                    raise ValueError("Введите число от '1' до '9'")
            except ValueError:
                print("Введите число от '1' до '9'")


    else:
        while True:
            try:
                player: int = int(input(f"Ходит игрок 2 {players_name["O"]}: "))
                if 1 <= player <= 9 and player not in entered_numbers:
                    first = False
                    second = True
                    symbol = "O"
                    entered_numbers.append(player)
                    break
                elif player in entered_numbers:
                    print("Это окно уже занято, выберите другое!")
                else:
                    raise ValueError("Введите число от '1' до '9'")
            except ValueError:
                print("Введите число от '1' до '9'")

    return player, symbol, first, second




def main():
    first_player_name: str = input("Игрок №1, введите Ваше имя: ")
    second_player_name: str = input("Игрок №2, введите Ваше имя: ")
    players_name: dict = {"X": first_player_name, "O": second_player_name}
    first = False
    second = True
    entered_numbers: list[int] = []
    while True:

        entered_number, symbol, *bools = get_players_input(first, second, entered_numbers, players_name)
        table = show_table(symbol, entered_number)
        res = check_winner(table)
        if res:
            break
        first = bools[0]
        second = bools[1]
    return res


result = main()

if result:
    player_choice: str = input("Хотите сыграть еще раз?(y/n) ")
    if player_choice == "y":


        main()


