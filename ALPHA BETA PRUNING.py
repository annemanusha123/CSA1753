def alphabeta(depth, node, alpha, beta, isMax):
    if depth == 3:
        return node

    if isMax:
        best = -999
        for child in [node*2, node*2+1]:
            best = max(best, alphabeta(depth+1, child, alpha, beta, False))
            alpha = max(alpha, best)
            if beta <= alpha:
                break   # Beta cut-off
        return best
    else:
        best = 999
        for child in [node*2, node*2+1]:
            best = min(best, alphabeta(depth+1, child, alpha, beta, True))
            beta = min(beta, best)
            if beta <= alpha:
                break   # Alpha cut-off
        return best

print("Optimal value:", alphabeta(0, 1, -999, 999, True))
