class Board:
    ALL_SPACES = list('123456789')  # Klucze słownika planszy KIK.
    X, O, BLANK = 'X', 'O', ' '  # Stałe reprezentujące wartości tekstowe.

    def __init__(self):
        self.gameBoard = self.get_blank_board()

    def get_blank_board(self):
        board = {}
        for space in self.ALL_SPACES:
            board[space] = self.BLANK
        return board

    def get_board_str(self):
        return f'''
                {self.gameBoard['1']}|{self.gameBoard['2']}|{self.gameBoard['3']} 1 2 3 
                -+-+- 
                {self.gameBoard['4']}|{self.gameBoard['5']}|{self.gameBoard['6']} 4 5 6 
                -+-+- 
                {self.gameBoard['7']}|{self.gameBoard['8']}|{self.gameBoard['9']} 7 8 9'''

    def is_valid_space(self, space):
        if space is None:
            return False
        return space in self.ALL_SPACES and self.gameBoard[space] == self.BLANK

    def is_winner(self, player):
        b, p = self.gameBoard, player
        return ((b['1'] == b['2'] == b['3'] == p) or  # poziomo na górze
                (b['4'] == b['5'] == b['6'] == p) or  # poziomo w środku
                (b['7'] == b['8'] == b['9'] == p) or  # poziomo u dołu
                (b['1'] == b['4'] == b['7'] == p) or  # pionowo z lewej
                (b['2'] == b['5'] == b['8'] == p) or  # pionowo w środku
                (b['3'] == b['6'] == b['9'] == p) or  # pionowo z prawej
                (b['3'] == b['5'] == b['7'] == p) or  # przekątna 1
                (b['1'] == b['5'] == b['9'] == p))  # przekątna 2

    def is_board_full(self):
        for space in self.ALL_SPACES:
            if self.gameBoard[space] == self.BLANK:
                return False
        return True

    def update_board(self, space, mark):
        self.gameBoard[space] = mark


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = self.board.X
        self.next_player = self.board.O

    def main(self):
        print('Witaj w grze kółko i krzyżyk!')

        while True:
            print(self.board.get_board_str())

            move = None
            move = self.make_move(move)
            print(move)
            self.board.update_board(move, self.current_player)

            if self.check_winner():
                break
            elif self.check_board_full():
                break

            self.switch_players()

        print('Dziękuję za grę!')

    def switch_players(self):
        self.current_player, self.next_player = self.next_player, self.current_player

    def make_move(self, move):
        while not self.board.is_valid_space(move):
            print(f'Jaki jest ruch gracza {self.current_player}? (1-9)')
            move = input()
        return move

    def check_winner(self):
        if self.board.is_winner(self.current_player):
            print(self.board.get_board_str())
            print(self.current_player + ' wygrał grę!')
            return True
        return False

    def check_board_full(self):
        if self.board.is_board_full():
            print(self.board.get_board_str())
            print('Gra zakończyła się remisem!')
            return True
        return False


if __name__ == '__main__':
    game = Game()
    game.main()
