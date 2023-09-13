class Player:
    def __init__(self, symbol):
        self.symbol = symbol

class TicTacToeModel:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = None
        self.winner = None

    def start_game(self):
        self.current_player = Player('X')

    def make_move(self, row, col):
        if self.board[row][col] == ' ' and not self.winner:
            self.board[row][col] = self.current_player.symbol
            if self.check_winner():
                self.winner = self.current_player
            else:
                self.current_player = Player('O') if self.current_player.symbol == 'X' else Player('X')

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

class TicTacToeView:
    def __init__(self):
        self.model = TicTacToeModel()

    def display_board(self):
        board = self.model.board
        for row in board:
            print(' | '.join(row))
            print('-' * 9)

    def get_player_move(self):
        row = int(input('Enter the row (0-2): '))
        col = int(input('Enter the column (0-2): '))
        return row, col

    def show_winner(self, winner):
        if winner:
            print(f"{winner.symbol} wins!")
        else:
            print("It's a tie.")

class TicTacToeController:
    def __init__(self):
        self.view = TicTacToeView()

    def start_game(self):
        self.view.model.start_game()
        self.view.display_board()
        while not self.view.model.winner:
            row, col = self.view.get_player_move()
            self.view.model.make_move(row, col)
            self.view.display_board()
        self.view.show_winner(self.view.model.winner)

if __name__ == '__main__':
    controller = TicTacToeController()
    controller.start_game()
