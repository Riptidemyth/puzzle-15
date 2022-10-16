import curses
from drawer import Drawer
from board import Board

def init_screen(scr):
    curses.curs_set(0)
    curses.mousemask(1)
    scr.keypad(1)
    scr.refresh()

def handle_input(scr):
    board = Board()
    drawer = Drawer(board)

    while True:
        scr.clear()
        drawer.draw_all(scr)
        ch = scr.getch()
        if ch == curses.KEY_RESIZE:
            curses.resizeterm(*scr.getmaxyx())
        elif ch == curses.KEY_MOUSE:
            _, mouse_x, mouse_y, _, _ = curses.getmouse()
            drawer.make_move((mouse_x, mouse_y))
        elif ch == ord('n'):
            board = Board()
            drawer.set_board(board)
            drawer.reset_counter() 
        elif ch == ord('r'):
            board.reset_board()
            drawer.reset_counter()
        elif ch == ord('h'):
            drawer.toggle_memo()
        elif ch == ord('e'):
            break

def main(scr):
    init_screen(scr)
    handle_input(scr)

curses.wrapper(main)
