class GameBoard:
    def __init__(self):
        self.cells = [' '] * 9
        self.turn = 'X'

    def show(self):
        print("\nCurrent board:")
        for i in range(0, 9, 3):
            row = ' | '.join(f'{self.cells[j] if self.cells[j] != " " else str(j)}' for j in range(i, i + 3))
            print(f'| {row} |')
        print()

    def place(self, pos):
        if 0 <= pos < 9 and self.cells[pos] == ' ':
            self.cells[pos] = self.turn
            self.turn = 'O' if self.turn == 'X' else 'X'
            return True
        return False

    def force_place(self, pos, ch):
        if 0 <= pos < 9 and self.cells[pos] == ' ':
            self.cells[pos] = ch
            return True
        return False

    def check_win(self, ch):
        lines = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        return any(all(self.cells[i] == ch for i in line) for line in lines)

    def is_draw(self):
        return ' ' not in self.cells and not self.check_winner()

    def check_winner(self):
        for player in ['X', 'O']:
            if self.check_win(player):
                return player
        return None

    def finished(self):
        return self.check_winner() is not None or self.is_draw()

    def free_spots(self):
        return [i for i in range(9) if self.cells[i] == ' ']

    def copy(self):
        new = GameBoard()
        new.cells = self.cells[:]
        new.turn = self.turn
        return new