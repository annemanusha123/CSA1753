def minimax(depth, node, isMax):
    if depth == 3:
        return node

    if isMax:
        return max(minimax(depth+1, node*2, False),
                   minimax(depth+1, node*2+1, False))
    else:
        return min(minimax(depth+1, node*2, True),
                   minimax(depth+1, node*2+1, True))

print("Optimal value:", minimax(0, 1, True))
