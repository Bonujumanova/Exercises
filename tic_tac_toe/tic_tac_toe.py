from colorama import init, Fore, Back, Style
init()


def show_current_table(data: list, char="", player_choice="") -> list:
    if char == "O":
        color = Fore.YELLOW
    else:
        color = Fore.GREEN
    height: int = len(data)
    width: int = len(data[0])
    for row in range(height):
        for col in range(width):
            if data[row][col] == player_choice:
                data[row][col] = char
            if col < (width - 1):
                print(data[row][col], "|", end=" ")
            else:
                print(str(data[row][col]))
        if row < (height - 1):
            print("----------")
    return data


def check_winner(changed_data: list[list]):

    for col in range(len(changed_data)):
        if all(changed_data[col][0] == changed_data[col][row] for row in range(len(changed_data[col]))):
            return "win", changed_data[col][0]

        for row in range(col, col + 1):
            if changed_data[0][row] ==  changed_data[1][row] == changed_data[2][row]:
                return "win", changed_data[0][row]

        if changed_data[0][0] == changed_data[1][1] == changed_data[2][2]:
            return "win", changed_data[1][1]

        elif changed_data[0][2] == changed_data[1][1] == changed_data[2][0]:
            return True, "win", changed_data[1][1]

    if all(all((str(j).isalpha() for j in i)) for i in changed_data):
        return "loss", None
    return False



def get_players_input(first: bool, second: bool, entered_numbers, players_name):
    if second:
        current_symbol: str = "X"
        second : bool= False
        first: bool = True
        player_num: int = 1
    else:
        current_symbol: str = "O"
        first: bool = False
        second: bool = True
        player_num: int = 2

    while True:
        try:
            player: int = int(input(f"Ходит игрок {player_num} {players_name["X"]}: "))
            if 1 <= player <= 9 and player not in entered_numbers:
                entered_numbers.append(player)
                break
            elif player in entered_numbers:
                print("Это окно уже занято, выберите другое!")
            else:
                raise ValueError
        except ValueError:
            print("Введите число от '1' до '9'")

    return player, current_symbol, first, second



def main():

    winner_text: dict[str, str] = {
        "win": "Победил игрок:",
        "loss": "Победителя нет! Постарайтесь выиграть в следующий раз!!!"
    }
    main_table: list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    show_current_table(main_table, )
    while True:
        try:
            first_player_name: str = input("Игрок №1, введите Ваше имя: ")
            second_player_name: str = input("Игрок №2, введите Ваше имя: ")
            if first_player_name == second_player_name:
                raise ValueError
        except ValueError:
            print("Не повторяйтесь! Выберите другое имя!")
        else:

            players_name: dict = {"X": first_player_name, "O": second_player_name}
            first = False
            second = True
            entered_numbers: list[int] = []
            table: list[list[int | str]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

            while True:
                entered_number, symbol, *bools = get_players_input(first, second, entered_numbers, players_name)
                table = show_current_table(table,symbol, entered_number)
                res = check_winner(table)

                if res:
                    winner_name: str = ""
                    if players_name.get(res[1]):
                        winner_name: str = players_name.get(res[1])
                    print(winner_text.get(res[0]), winner_name)
                    break

                first = bools[0]
                second = bools[1]
            return res


result = main()

while result:
    player_choice: str = input("Хотите сыграть еще раз?(y/n) ")
    if player_choice == "y":
        result = main()
    else:
        break



