data: list[list[int | str]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for col in range(len(data)):
    for row in range(len(data[col])):
        if row != 2:
            print(data[col][row], "|", end=" ")
        else:
            print(data[col][row])
    print("-----------")



def show_table(char: str, player_choice: int) -> list:
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
                print(f"Пебедил игрок: {players.get(changed_data[col][row])}, '2'")
                return True

        if changed_data[col][0] == changed_data[col][1] == changed_data[col][2]:
            print(f"Пебедил игрок: {players.get(changed_data[col][1])} '3'")
            return True
        elif changed_data[col][2] == changed_data[col][1] == changed_data[col][0]:
            print(f"Пебедил игрок: {players.get(changed_data[col][1])} '4'")
            return True

    return False

count = 0
second = True
def main():
    global count
    global second
    players: dict = {"X": "player_1_name", "O": "player_1_name"}


    while True:

        if second:
            player: int = int(input(f"Ходит игрок 1 {players["X"]}: "))
            second = False
            symbol = "O"

        else:
            player: int = int(input(f"Ходит игрок 2 {players["O"]}: "))
            second = True
            symbol = "X"


        table = show_table(symbol, player)
        res = check_winner(table)
        if res:
            break


main()

