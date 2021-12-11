import numpy as np

def part1(board):
    flashes = 0

    for i in range(0, 100):
        flashed = []
        nines = [(i, j) for i in range(0, len(board)) for j in range(0, len(board[0])) if board[i][j] == 9]

        while len(nines) > 0:
            el = nines[0]
            nines.remove(el)

            if el not in flashed:
                flashes += 1
                flashed.append(el)

                new_nines = flash_board(el, board)
                nines.extend(new_nines)
        for j in range(0, len(board)):
            for k in range(0, len(board[0])):
                board[j][k] += 1
        for j in flashed:
            board[j[0]][j[1]] = 0

    print(flashes)


def part2(board):
    flashes = 0
    synch_idx = 0
    complete_flash = False

    while not complete_flash:
        synch_idx += 1
        flashed = []
        nines = [(i, j) for i in range(0, len(board)) for j in range(0, len(board[0])) if board[i][j] == 9]

        while len(nines) > 0:
            el = nines[0]
            nines.remove(el)

            if el not in flashed:
                flashes += 1
                flashed.append(el)

                new_nines = flash_board(el, board)
                nines.extend(new_nines)
        for j in range(0, len(board)):
            for k in range(0, len(board[0])):
                board[j][k] += 1
        for j in flashed:
            board[j[0]][j[1]] = 0

        complete_flash = check_synch(board)

    print(synch_idx)


def check_synch(board):
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] != 0:
                return False
    return True


def flash_board(el, board):
    ret = []

    for i in range(max(el[0] - 1, 0), min(el[0] + 2, len(board))):
        for j in range(max(el[1]-1, 0), min(el[1] + 2, len(board[0]))):
            if not (i == el[0] and j == el[1]):
                board[i][j] += 1
                if board[i][j] >= 9:
                    ret.append((i, j))

    return ret


lines = open("input.txt").readlines()
mat = []
for line in lines:
    to_append = [int(char) for char in line.rstrip()]
    mat.append(to_append)
mat2 = np.copy(mat)
part1(mat)
part2(mat2)