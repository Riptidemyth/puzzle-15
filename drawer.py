class Drawer:
    memo_needed = True
    move_number = 0
    board = None
    min_button_width = 4
    min_button_height = 3
    button_width = 0
    button_height = 0

    def __init__(self, board):
        self.board = board

    def draw_all(self, scr):
        memo_width = self.draw_memo(scr)
        move_counter_width = self.draw_move_counter(scr)
        self.draw_board(scr, max(memo_width, move_counter_width) + 1)

    def draw_memo(self, scr):
        if not self.memo_needed:
            return 0

        scr_y, scr_x = scr.getmaxyx()
    
        memo = [
            "Controls:",
            "Use left mouse button to move tiles around",
            "Resize the window to change board size as needed",
            "n - Start new game (new setup)",
            "r - Restart game from the beginning (same setup)",
            "h - Hide/Show this memo",
            "e - Exit"
        ]

        memo_width = max(*[len(s) for s in memo])
        memo_height = len(memo)
        
        memo_x = scr_x - max(*[len(s) for s in memo])
        memo_y = 0

        if memo_x < 0 or memo_height > scr_y:
            return 0

        for i in range(len(memo)):
            scr.addstr(memo_y + i, memo_x, memo[i])

        return memo_width

    def toggle_memo(self):
        self.memo_needed = not self.memo_needed

    def draw_move_counter(self, scr):
        scr_y, scr_x = scr.getmaxyx()

        move_counter_str = "Moves: " + str(self.move_number)
        move_counter_x = scr_x - len(move_counter_str) - 1
        move_counter_y = scr_y - 1

        if move_counter_x < 0:
            return 0

        scr.addstr(move_counter_y, move_counter_x, move_counter_str)

        return len(move_counter_str)

    def draw_board(self, scr, right_padding):
        scr_y, scr_x = scr.getmaxyx()
        board_width = scr_x - right_padding
        board_height = scr_y
        self.button_width = board_width // 4
        self.button_height = board_height // 4

        if self.button_width < self.min_button_width or self.button_height < self.min_button_height:
            return

        for i in range(self.board.length()):
            title = self.board.get(i)
            if title != 0:
                self.draw_button(scr, title, i)

    def draw_button(self, scr, title, index):
        x, y = self.convert_index_to_coords(index)
        self.draw_frame(scr, index)
        scr.addstr(y + self.button_height // 2, x + self.button_width // 2, str(title))

    def draw_frame(self, scr, index):
        x, y = self.convert_index_to_coords(index)
        scr.addstr(y, x, '*' * self.button_width)
        scr.addstr(y + self.button_height - 1, x, '*' * self.button_width)
        for i in range(self.button_height):
            scr.addstr(y + i, x, '*')
            scr.addstr(y + i, x + self.button_width - 1, '*')

    def convert_index_to_coords(self, index):
        x, y = index % self.board.get_dimention(), index // self.board.get_dimention()
        x *= self.button_width
        y *= self.button_height
        return (x, y)

    def convert_coords_to_index(self, coords):
        x, y = coords
        return y // self.button_height * self.board.get_dimention() + x // self.button_width

    def set_board(self, board):
        self.board = board

    def reset_counter(self):
        self.move_number = 0

    def make_move(self, coords):
        if self.board.make_move(self.convert_coords_to_index(coords)):
            self.move_number += 1

