import time
global N
# initialize the board


def printboard(b):
    num = len(b)
    for i in range(num):
        for j in range(num):
            if b[i] == j:
                print('1', end=' ')
            else:
                print('0', end=' ')
        print()

# Final test function


def finaltest(board):
    num = len(board)
    if num > 1:
        for i in range(num-1, 0, -1):
            for j in range(i-1, -1, -1):
                # checking Down
                if board[i] == board[j]:
                    return False
                # checking left diagonal up
                if board[i] == board[j]+(i-j):
                    return False
                # checking right diagonal up
                if board[i] == board[j]-(i-j):
                    return False
    return True


def isSafe(current, j, level):
    if(len(current[0]) != 0):
        lookUp = current[1]
        if j in lookUp[level-1]:
            return False
    return True


def constructLookUp(position, table, level):

    global N
    if(len(table) == 0):
        table = []
        for i in range(N-1):
            table.append(set())
    # no down
    for i in range(level, N):
        table[i-1].add(position)

    # no diagonal down right
    for i in range(level, N-position):
        table[i-1].add(position+i)
    # no diagonal down left
    for i in range(level, level+position):
        table[i-1].add(position-i)
    return table


def bfs(board):
    # initial state
    global N
    queue = []
    queue.append(board)
    while True:
        current = queue.pop(0)
        level = len(current[0])
        if level != N:
            for j in range(N):
                if isSafe(current, j, level):
                    newBoard = current[0][:]
                    newBoard.append(j)
                    table = constructLookUp(j, current[1], level+1)
                    queue.append((newBoard, table))

        else:
            queue.insert(0, current)
            break
    return queue


def main():
    global N
    board = ([], [])

    N = int(input('Enter N: '))
    # initialize the board
    # for i in range(N):
    #     row = [-1] * N
    #     board.append(row)

    start = time.time()
    final = bfs(board)
    stop = time.time() - start
    print('Results: ' + str(len(final)))
    print('Time: {:.4}'.format(stop))


main()
