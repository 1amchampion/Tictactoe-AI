"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # keep count of all the moves on the board.
    # if the board is empty: x 
    # if xCount > oCount : o 
    # else: x 

    xCount = 0
    oCount = 0
    mtyCount = 0

    for rows in board:
        for cell in rows:
            if cell == EMPTY:
                mtyCount += 1
            if cell == X:
                xCount += 1
            if cell == O:
                oCount += 1

    if mtyCount == 9 or oCount >= xCount:
        return X
    else: 
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    gActions = set()

    # every EMPTY space on the board is a possible action 
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                gActions.add((i, j))
    
    return gActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    import copy 
    newBoard = copy.deepcopy(board)

    pTurn = player(board)

    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise Exception("Invalid Position")
    
    elif newBoard[action[0]][action[1]] == EMPTY:
        newBoard[action[0]][action[1]] = pTurn

    else:
        raise Exception("Invalid Position")

    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # the winner is a player that has a 3 in a row.
    # I guess I have to run check for all the 8 winning states

    # xxx
    # ---
    # ---
    if board[0][0] == board[0][1] == board[0][2] != None:
        return board[0][0]
    # ---
    # xxx
    # ---
    elif board[1][0] == board[1][1] == board[1][2] != None:
        return board[1][0]
    # ---
    # ---
    # xxx
    elif board[2][0] == board[2][1] == board[2][2] != None:
        return board[2][0]
    # x--
    # x--
    # x--
    elif board[0][0] == board[1][0] == board[2][0] != None:
        return board[0][0]
    # -x-
    # -x-
    # -x-
    elif board[0][1] == board[1][1] == board[2][1] != None:
        return board[0][1]
    # --x
    # --x
    # --x
    elif board[0][2] == board[1][2] == board[2][2] != None:
        return board[0][2]
    # --x
    # -x-
    # x--
    elif board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]
    # x--
    # -x-
    # --x
    elif board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    
    # game is over is all the spaces on the board are not empty 
    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    victor = winner(board)
    if victor == X:
        return 1
    elif victor == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board): 
        return None

    if player(board) == X:
        v = -float("inf")
        bestAction = (0, 0)
    
        for action in actions(board):
            actionUtility = minValue(result(board, action))
            if actionUtility > v:
                v = actionUtility
                bestAction = action
        return bestAction

    elif player(board) == O:
        v = float("inf")
        bestAction = (0, 0)

        for action in actions(board):
            actionUtility = maxValue(result(board, action))
            if actionUtility < v:
                v = actionUtility
                bestAction = action
        return bestAction
    
    else: 
        return None
    

def maxValue(board):
    if terminal(board): 
        # print(f"max board utility: {utility(board)}")
        # print('\n')
        return utility(board)
    
    v = -float('inf')
    for action in actions(board):
        # print (f'max action: {action}')
        # print (f'max board: {result(board, action)}')
        v = max(v, minValue(result(board, action)))
        # print(f'max utility: {v}')
    return v


def minValue(board):
    if terminal(board):
        # print(f"min board utility: {utility(board)}")
        # print('\n')
        return utility(board)
    
    v = float('inf')
    for action in actions(board):
        # print (f'min action: {action}')
        # print (f'min board: {result(board, action)}')
        v = min(v, maxValue(result(board, action)))
        # print(f'min utility: {v}')
    return v
