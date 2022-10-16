import random
import copy

class Board:
    initial_board = None
    board = None
    possible_moves = None
    blank_index = 0
    n = 4

    def __init__(self):
        self.initial_board = self.generate_board()
        self.board = copy.deepcopy(self.initial_board)
    
    def get_possible_moves(self):
        # for explanations below INDEX refers to a blank hole index
        possible_moves = []
        index = self.blank_index
        # index mod n == 0 means index has the leftmost position in a row
        # if it is not, the move from the cell directly to the left is possible
        if not (index % self.n == 0):
            possible_moves.append(index - 1)
        # index mod n == n - 1 means index has the rightmost position in a row
        # if it is not, the move from the cell directly to the right is possible
        if not (index % self.n == self.n - 1):
            possible_moves.append(index + 1)
        # index < n means index position is in the 1st row
        # if it is not, the move from the cell directly above it is possible
        if not (index < self.n):
            possible_moves.append(index - self.n)
        # index >= n * n - 1 means index position is in the last row
        # if it is not, the move from the cell directly below it is possible
        if not (index >= self.n * (self.n - 1)):
            possible_moves.append(index + self.n)
        return possible_moves

    # Board generation algorithm inspired by http://kevingong.com/Math/SixteenPuzzle.html
    #
    # For 4x4 board 2 theorems are used from the link above:
    # THEOREM 1.1b: If n is even, then every legal configuration with the hole in row i where n - i is even
    #               corresponds to a permutation with an even number of inversions.
    # THEOREM 1.1c: If n is even, then every legal configuration with the hole in row i where n - i is odd
    #               corresponds to a permutation with an odd number of inversions.
    #
    # So, to generate a legal configuration the following actions are made:
    # 1. Generate random sequence and blank hole index.
    # 2. Calculate number of inversions in generated random permutation
    # 3. Check whether blank hole index is odd or even and check whether number of inversions in sequence
    #    is odd or even.
    # 4. If needed, add/remove one inversion to change number of inversions from odd to even or vice versa.
    #    The easiest way to do it is to swap elements 1 and 2, since this change is guaranteed to add or remove
    #    exactly one inversion.
    def generate_board(self):
        board = [i for i in range(1, self.n * self.n)]
        random.shuffle(board)
        self.blank_index = random.choice(range(len(board)))
        self.possible_moves = self.get_possible_moves()
        inversions = self.calculate_inversions(board)

        if self.blank_index // 4 % 2 == inversions % 2:
            board[board.index(1)], board[board.index(2)] = board[board.index(2)], board[board.index(1)]
        board.insert(self.blank_index, 0)

        self.board = board
        return self.board

    def make_move(self, index):
        if index in self.possible_moves:
            self.board[self.blank_index], self.board[index] = self.board[index], self.board[self.blank_index]
            self.blank_index = index
            self.possible_moves = self.get_possible_moves()
            return True
        else:
            return False

    # TODO: this function's complexity is O(n^2), however O(n*log n) is possible, further optimization can be done
    def calculate_inversions(self, row):
        inversions = 0
        for i in range(len(row)):
            for j in range(i, len(row)):
                if row[i] > row[j]:
                    inversions += 1
        return inversions

    def reset_board(self):
        self.board = copy.deepcopy(self.initial_board)
        self.blank_index = self.board.index(0)
        self.possible_moves = self.get_possible_moves()

    def length(self):
        return len(self.board)

    def get(self, i):
        return self.board[i]

    def get_dimention(self):
        return self.n
