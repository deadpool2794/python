def isValid(board):
    d = {}
    d['X'] = 0
    d['O'] = 0
    d['-'] = 0
    for i in board:
        for j in i:
            d[j] += 1
    if d['X'] - d['O'] > 1:
        return 'No'

    ct_X, ct_O = 0, 0
    for i in board:
        st = ''
        for j in i:
            st += j
        if st == 'XXX':
            ct_X += 1
        if st == 'OOO':
            ct_O += 1
    
    if board[0][0]+board[1][1] + board[2][2] == 'XXX':
        ct_X += 1
    if board[0][0]+board[1][1] + board[2][2] == 'OOO':
        ct_O += 1
    if board[0][2]+board[1][1] + board[2][0] == 'XXX':
        ct_X += 1
    if board[0][2]+board[1][1] + board[2][0] == 'OOO':
        ct_O += 1
    
    for i in range(3):
        st = ''
        for j in range(3):
            st += board[j][i]
        if st == 'XXX':
                ct_X += 1
        if st == 'OOO':
                ct_O += 1
    
    if (ct_O > 0 and ct_X > 0) or ct_X > 1 or ct_O > 1:
        return 'No'
    return 'Yes'


board = []
for _ in range(3):
    row = input()
    board.append(list(row))

print(isValid(board))
