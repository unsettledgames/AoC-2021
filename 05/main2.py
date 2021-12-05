board = []
board_size = 2000


def reset_board():
    global board
    for i in range(0, board_size):
        to_append = []
        for j in range(0, board_size):
            to_append.append(0)
        board.append(to_append)


def draw_line(x1, x2, y1, y2):
    global board

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    if not (x1 == x2 or y1 == y2):
        if y1 - y2 < 0:
            #Top left -> Bottom right
            for i in range(x1, x2 + 1):
                board[i][y1 + i-x1] += 1
        else:
            #Bottom left -> top right
            for i in range(x1, x2 + 1):
                board[i][y1 - (i-x1)] += 1
        return

    if y1 > y2:
        y1, y2 = y2, y1
        x1, x2 = x2, x1

    if x1 == x2:
        for i in range(y1, y2+1):
            board[x1][i] += 1
    else:
        for i in range(x1, x2+1):
            board[i][y1] += 1


def count_overlapping():
    global board
    ret = 0

    for i in range(0, board_size):
        for j in range(0, board_size):
            if board[i][j] > 1:
                ret += 1
    return ret


inputLines = open("input.txt").readlines()
lines = [tuple(line.replace("\n","").split(" -> ")) for line in inputLines]

reset_board()
for line in lines:
    draw_line(int(line[0].split(",")[0]), int(line[1].split(",")[0]), int(line[0].split(",")[1]), int(line[1].split(",")[1]))
print(count_overlapping())