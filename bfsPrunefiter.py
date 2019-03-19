import time
global N
# initialize the board

# Function to reconstruct the board


def printboard(b):
    num = len(b)
    for i in range(num):
        for j in range(num):
            if b[i] == j:
                print('1', end=' ')
            else:
                print('0', end=' ')
        print()

# Final test function - Without pruning


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

# Check for valid positions in the next row to place a queen


def checkPos(board):
    global N
    if len(board) == 0:
        return [-1]
    nextLevel = len(board) + 1
    invalid = set()
    for i in range(len(board)):
        pos = board[i]
        # predict col
        invalid.add(pos)
        # predict diagonal down right
        r = pos + nextLevel - i - 1
        if r < N:
            invalid.add(r)
        # predict diagonal down left
        r = pos - (nextLevel - i - 1)
        if r >= 0:
            invalid.add(r)

    return invalid


def bfs(board):
        # initial state
    global N
    queue = []
    queue.append(board)

    while True:
        current = queue.pop(0)
        level = len(current)

        if level != N:
            inval = checkPos(current)
            for j in range(N):
                if not j in inval:
                    newBoard = current[:]
                    newBoard.append(j)
                    # if finaltest(newBoard):
                    queue.append(newBoard)
        else:
            queue.insert(0, current)
            break
    return queue


def bfsHigh(board):
        # initial state
    global N
    queue = []
    queue.append(board)
    solution = 0
    while len(queue) != 0:
        current = queue.pop(0)
        level = len(current)
        inval = checkPos(current)
        if level < N-1:
            for j in range(N):
                if not j in inval:
                    newBoard = current[:]
                    newBoard.append(j)
                    queue.append(newBoard)
        else:
            solution += N - len(inval)
    return solution


def main():
    global N
    board = []

    N = int(input('Enter N: '))

    start = time.time()
    solutions = bfsHigh(board)
    stop = time.time() - start
    print('Results: ' + str(solutions))
    print('Time: {:.4}'.format(stop))


# def main():
#     global N
#     board = []

#     N = int(input('Enter N: '))

#     start = time.time()
#     final = bfs(board)
#     stop = time.time() - start
#     print('Results: ' + str(len(final)))
#     print('Time: {:.4}'.format(stop))
#     if(N < 7):
#         for f in final:
#             print(f)
#             printboard(f)
#             s = '-' * N
#             print(s)


main()
