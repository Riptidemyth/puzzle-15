from board import Board
import random

def run_test_functions(*test_functions):
    failed = []
    print('Running', len(test_functions), 'tests')
    for f in test_functions:
        if f():
            print('.', end = '')
        else:
            print('x', end = '')
            failed.append(f.__name__)
    print()
    if len(failed) == 0:
        print('All tests succeeded')
    else:
        print(len(failed), 'test(s) failed:')
        for f in failed:
            print(f)

def test_calculate_inversions():
    board = Board()
    if board.calculate_inversions([4, 5, 1, 3, 2]) != 7:
        return False
    if board.calculate_inversions([7, 2, 1, 4, 6, 3, 5]) != 10:
        return False
    return True

def test_get_possible_moves():
    board = Board()
    board.blank_index = 0
    if sorted(board.get_possible_moves()) != [1, 4]:
        return False
    return True

def test_make_move():
    board = Board()
    index_to_move = random.choice(board.possible_moves)
    board.make_move(index_to_move)
    if board.blank_index != index_to_move:
        return False
    if board.get_possible_moves() != board.possible_moves:
        return False
    return True

run_test_functions(
    test_calculate_inversions,
    test_get_possible_moves,
    test_make_move
)
