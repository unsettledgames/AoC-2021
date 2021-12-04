boards = {}


def print_mat(mat):
    for i in range(0, 5):
        print(mat[i])


def compute_win(board, last_drawn):
    sum = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if board[i][j] > 0:
                sum += board[i][j]
    print(str(last_drawn * sum) + "\n")


def update_boards(num):
    for k in boards.keys():
        for i in range(0, 5):
            for j in range(0, 5):
                if boards[k][i][j] == num:
                    boards[k][i][j] = -1
                    if check_win(k):
                        compute_win(boards[k], num)
                        return True

    return False


def check_win(board_key):
    board = boards[board_key]

    # Check rows
    for i in range(0, 5):
        same = True
        for j in range(0, 5):
            if board[i][j] >= 0:
                same = False
                break
        # Win by row
        if same:
            return True

    #Check rows
    for i in range(0, 5):
        same = True
        for j in range(0, 5):
            if board[j][i] >= 0:
                same = False
                break
        if same:
            return True
    return False


lines = open("input.txt", "r").readlines()
drawn = str(lines[0]).split(",")
i = 0
curr_mat = []

for line in lines:
    if line == lines[0]:
        continue
    if i % 6 == 0 and i != 0:
        boards[str(round(i / 6))] = curr_mat
        curr_mat = []

    if line != "" and line != "\n":
        nums = line.split(" ")
        curr_line = [int(num) for num in nums if num != " " and num != ""]
        curr_mat.append(curr_line)
    i += 1
boards[str(round(i / 6))] = curr_mat

for num in drawn:
    if update_boards(int(num)):
        break

# for k in boards.keys():
#     print_mat(boards[k])
#     print("\n")