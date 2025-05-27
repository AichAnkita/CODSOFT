import math
def score(board):
    winner = board.check_winner()
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    return 0

def minimax(board, is_ai):
    result = score(board)
    if board.finished():
        return result

    if is_ai:
        best = -math.inf
        for move in board.free_spots():
            clone = board.copy()
            clone.place(move)
            best = max(best, minimax(clone, False))
        return best
    else:
        worst = math.inf
        for move in board.free_spots():
            clone = board.copy()
            clone.place(move)
            worst = min(worst, minimax(clone, True))
        return worst

def ai_pick(board):
    best_val = -math.inf
    best_move = None
    for move in board.free_spots():
        clone = board.copy()
        clone.place(move)
        val = minimax(clone, False)
        if val > best_val:
            best_val = val
            best_move = move
    return best_move