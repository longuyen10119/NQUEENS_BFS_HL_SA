import time
global N

# Print board function
# Reconstruct the board from 1d array


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


def bfs(board):
    # initial state
    global N
    queue = []
    queue.append(board)

    while True:
        current = queue.pop(0)
        if len(current) != N:
            for j in range(N):
                newBoard = current[:]
                newBoard.append(j)
                queue.append(newBoard)
        else:
            queue.insert(0, current)
            break
    return queue


def main():
    global N

    val = int(input('Enter N: '))

    for i in range(4, val+1):
        N = i
        board = []
        start = time.time()
        final = bfs(board)
        results = []
        # Test all possible solutions BFS returns
        for f in final:
            if finaltest(f):
                results.append(f)
        stop = time.time() - start
        print('WHEN N = {}'.format(i))
        print('Results: ' + str(len(results)))
        print('Time: {:.4f}'.format(stop))
        if(i < 7):
            for r in results:
                # print(r)
                printboard(r)
                s = '--' * N
                print(s)
        s = '_________________________________'
        print(s)


main()
