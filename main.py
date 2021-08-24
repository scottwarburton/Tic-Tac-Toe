
position = {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
empty_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def display_board():
    # show the current board

    board = f" {position[1]} | {position[2]} | {position[3]} \n-----------\n {position[4]} | {position[5]} | {position[6]} \n-----------\n {position[7]} | {position[8]} | {position[9]} "
    print(board)


def player_choice(player):
    # receive position choice input, validate choice, put player's marker on board

    position_choice = None

    while position_choice not in empty_positions:

        position_choice = input("Select an empty position (1 to 9): ")

        if not position_choice.isdigit():
            print("Your choice must be a number\n")
            continue

        position_choice = int(position_choice)

        if position_choice not in range(1, 10):
            print("Your choice must be within 1 to 9\n")
            continue

        if position_choice in empty_positions:
            position[position_choice] = player
            empty_positions.remove(position_choice)
            break
        else:
            print("Your choice must be a free position on the board\n")
            continue

    display_board()


def winner_found():
    # check markers for a winner

    winner = None
    marker_list = []

    marker_list.append(position[1] + position[2] + position[3])
    marker_list.append(position[4] + position[5] + position[6])
    marker_list.append(position[7] + position[8] + position[9])
    marker_list.append(position[1] + position[4] + position[7])
    marker_list.append(position[2] + position[5] + position[8])
    marker_list.append(position[3] + position[6] + position[9])
    marker_list.append(position[1] + position[5] + position[9])
    marker_list.append(position[3] + position[5] + position[7])

    if marker_list.count("XXX") > 0:
        winner = "Player X"
    elif marker_list.count("OOO") > 0:
        winner = "Player O"
    return winner


def Welcome():
    print("Welcome to Tic Tac Toe!\n")

    print("Here is the Board. Positions are marked to help you choose where to put your marker: \n")

    board = f" {1} | {2} | {3} \n-----------\n {4} | {5} | {6} \n-----------\n {7} | {8} | {9} "
    print(board)

    print("Player X goes first. Good luck!\n")


def TicTacToe():
    # game play

    Welcome()

    turn = 1

    while not winner_found():

        if turn in range(1, 11, 2):
            player = "X"
        else:
            player = "O"

        print("\nIt's your turn Player " + player + "\n")

        player_choice(player)

        turn += 1

        if turn == 10:
            return "It's a draw!"

    return "Congratulations " + winner_found() + ", you win!"

TicTacToe()