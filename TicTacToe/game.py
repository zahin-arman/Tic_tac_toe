from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        # This is jst getting the rows
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # return [i for i, spot in enumerate(self.board) if spot == ' ']
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board

    def number_of_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal_1]):
                return True
            diagonal_2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal_2]):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'  # Starting Letter.

    while game.empty_squares():

        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print('')  # just empty line

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            letter = "O" if letter == "X" else "X"
            time.sleep(1)

    if print_game:
        print("It's a tie!")


if __name__ == '__main__':
    print("Welcome to Tic Tac Toe. We have 3 game mode \n1.Player vs Player \n"
          "2.Player vs Computer (Easy)\n"
          "3.Player vs Computer (Hard)\n")
    gamemode = input("Choose one game mode with (1, 2, 3): ")

    if gamemode == '1':
        x_player = HumanPlayer('X')
        o_player = HumanPlayer('O')
        t = TicTacToe()
        play(t, x_player, o_player)
    elif gamemode == '2':
        x_player = HumanPlayer('X')
        o_player = RandomComputerPlayer('O')
        t = TicTacToe()
        play(t, x_player, o_player)
    elif gamemode == '3':
        x_player = HumanPlayer('X')
        o_player = GeniusComputerPlayer('O')
        t = TicTacToe()
        play(t, x_player, o_player)
    else:
        print("Please type in (1 or 2 or 3)")
