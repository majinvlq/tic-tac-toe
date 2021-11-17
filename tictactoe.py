"""
This is a simple tic-tac-toe game.
Has to be opened in command prompt.
"""
import random


def main():
    """Main script to run the program, parameters and function libs."""
    empty_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    instruction_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    start_game = True
    game_status = False

    def display_board(board):
        """
        Function to print out the game board.

        :param:
            board - list
        :return:
            prints 100 empty lines
            prints 3 lines of board (list split by indices).
        """
        print('\n' * 100)
        print(board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('--|---|--')
        print(board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('--|---|--')
        print(board[1] + ' | ' + board[2] + ' | ' + board[3])

    def game_starter():
        """
        Initiation of the game than runs when starting the script.
        Awaits the input of the player to choose if to start the game or not.


        :return game_on: bool to allow the whole game loop running
        :return START_GAME: bool True to initiate the game, False to close the game
        """
        print('\n' * 50)
        display_board(game_board)
        print("Welcome to Tic Tac Toe game\n")
        game_on = False

        while not game_on:
            question = input("Do you want to start? [Y/N] ")
            question = question.capitalize()
            if question == 'Y':
                game_on = True
                display_board(instruction_board)
                print("You will be picking X or O position by inserting the position number.")
                print("Please see the graph above.")
            elif question == 'N':
                print("\nOk, see you next time!\n")
                break
            else:
                print("You have to answer Y or N.\n")
                continue
        return game_on

    def player_input():
        """
        Defines markers assignment.
        One of the player inputs first marker. Program automatically assign the other.

        :return:
            player1_marker (str) - marker of the first player
            player2_marker (str) - marker of the second player
        """
        player1_marker = ""
        player2_marker = ""
        markers = ['X', 'O']

        print("\nLets play a game!\n")

        while player1_marker not in markers:

            player1_marker = input("\nWould you like to be X or O? ")
            player1_marker = player1_marker.capitalize()

            if player1_marker == "X":
                player2_marker = "O"
            elif player1_marker == "O":
                player2_marker = "X"
            else:
                print("Sorry, you have to pick X or O. Try again.\n")
                continue
        print(f"\nYou are Player 1 and have {player1_marker}'s")
        print(f"Your colleague is Player 2 and has {player2_marker}'s\n")
        return player1_marker, player2_marker

    def choose_first():
        """
        Function randomizing which player starts first.

        :return:
            current_player (int): integer to show which player is starting first
        """
        starting_player = random.randint(1, 2)
        print(f'Player {starting_player} is choosing first!')
        return starting_player

    def player_choice(player, board):
        """
        Defines the current player choice on which position marker shall be placed.
        Checks if the current choice is in range 1-9.
        Verifies if the chosen position is occupied or not, using space_check() function.

        :param player: int, number of a current player
        :param board: list, actual state of the game board
        :return: choice (int): position that current player chooses
        """
        choice = ''
        acceptable_range = range(1, 10)
        within_range = False

        while not choice.isdigit() or not within_range:
            choice = input(f"Player {player} - choose your position on board (1-9): ")

            if not choice.isdigit():
                print("Your choice is not in a digit format \n")

            if choice.isdigit():
                if int(choice) in acceptable_range:
                    within_range = space_check(board, int(choice))
                else:
                    within_range = False
                    print("Your choice is outside acceptable range (1-9)\n")

        return int(choice)

    def space_check(board, choice):
        """
        Checks if the chosen position on board is occupied

        :param board: current state of the game board
        :param choice: current player's choice (x or o)
        :return: bool used in player_choice() function confirming if their choice was right
        """
        if board[choice] != " ":
            print("This position is taken, choose another one.\n")
            return False
        return True

    def player_marker(player):
        """
        Returns a specific marker to be placed in position on board
        depending on which players' turn is now.

        :param player: takes in the current player number
        :return: marker (str) of the current player assigned to earlier defined player_marker
        """
        p_marker = ''
        if player == 1:
            p_marker = p1_mark
        elif player == 2:
            p_marker = p2_mark
        else:
            pass
        return p_marker

    def place_marker(board, mark, pos):
        """
        Places current player's marker on the actual game board.

        :param board: list - actual board
        :param mark: str - current player marker (x or o)
        :param pos: int - chosen position on the board
        :return:
            board - updated game board after marker assignment in position
        """
        board[pos] = mark
        return board

    def full_board_check(board):
        """
        Checks if the board is full.

        :param board: actual state of the game board
        :return: bool saying if the board is already full (True) or not yet (False)
        """
        full_board_counter = 0
        for i in board:
            if i in ('X', 'O'):
                full_board_counter += 1
            else:
                pass
        return full_board_counter == 9

    def win_check(board, mark):
        """
        Check if the game has been won after the last marker placement. If not, script continues.

        :param board: list - actual state of the board
        :param mark: str - the current mark that's in play
        :return: bool for the function, True - game is won, False - game continues
        """
        return (board[1] == board[4] == board[7] == mark) or \
               (board[2] == board[5] == board[8] == mark) or \
               (board[3] == board[6] == board[9] == mark) or \
               (board[1] == board[2] == board[3] == mark) or \
               (board[4] == board[5] == board[6] == mark) or \
               (board[7] == board[8] == board[9] == mark) or \
               (board[1] == board[5] == board[9] == mark) or \
               (board[3] == board[5] == board[7] == mark)

    def player_swap(player):
        """Swaps the current_player number. Returns new current_player number."""
        if player == 1:
            player = 2
        else:
            player = 1
        return player

    def replay():
        """
        Awaits the players decision(input) if to play again or not.

        :return: bool - True if to continue, False to stop
        """
        dec = False
        decisions = ['Y', 'N']

        while not dec:
            decision = input("\nDo you want to play again? [Y/N]:\n")
            decision = decision.capitalize()
            if decision in decisions:
                return decision == 'Y'
            print("I do not understand, can you answer again?\n")

    def clear_board(clean_b):
        """Clears the board of the game"""
        board = clean_b
        return list(board)

    # GAME STARTS HERE
    while start_game:
        game_started = game_starter()
        while game_started:
            p1_mark, p2_mark = player_input()
            current_player = choose_first()
            while not game_status:
                display_board(game_board)
                position = player_choice(current_player, game_board)
                marker = player_marker(current_player)
                place_marker(game_board, marker, position)
                full_board_check(game_board)
                if win_check(game_board, marker):
                    display_board(game_board)
                    print(f'Player {current_player} has won!')
                    game_status = True
                    break
                if full_board_check(game_board) and not win_check(game_board, marker):
                    display_board(game_board)
                    print("It's a TIE!")
                    game_status = True
                    break
                current_player = player_swap(current_player)
            game_board = clear_board(empty_board)
            result = replay()
            if result:
                game_status = False
                game_started = True
            else:
                print("Thanks, GGs!")
                game_started = False
        break


if __name__ == "__main__":
    main()
