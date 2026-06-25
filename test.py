from tictactoe import minimax, result

X = "X"
O = "O"
EMPTY = None

board = [
    [EMPTY, X, O],
    [O, X, EMPTY],
    [X, EMPTY, O]
]
action = (2, 4)

print(result(board, action))
# print(terminal(board))
# print(winner(board))
# print(utility(board))
minimax(board)