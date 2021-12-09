
def part1(board):
    low_points = []

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            val = board[i][j]

            # Top left
            if i == 0 and j == 0:
                if board[i][j+1] > val and board[i+1][j] > val:
                    low_points.append((i, j))
            # Top
            elif i == 0 and j != len(board[0])-1:
                if board[i][j+1] > val and board[i+1][j] > val and board[i][j-1] > val:
                    low_points.append((i, j))
            # Top right
            elif i == 0 and j == len(board[0])-1:
                if board[i][j-1] > val and board[i+1][j] > val:
                    low_points.append((i, j))
            # Left
            elif i != len(board)-1 and j == 0:
                if board[i+1][j] > val and board[i-1][j] > val and board[i][j+1] > val:
                    low_points.append((i, j))
            # Right
            elif i != len(board)-1 and j == len(board[0])-1:
                if board[i+1][j] > val and board[i-1][j] > val and board[i][j-1] > val:
                    low_points.append((i, j))
            # Bottom left
            elif  i == len(board)-1 and j == 0:
                if board[i-1][j] > val and board[i][j+1] > val:
                    low_points.append((i, j))
            # Bottom
            elif i == len(board)-1 and j != len(board[0])-1:
                if board[i][j+1] > val and board[i][j-1] > val and board[i-1][j] > val:
                    low_points.append((i, j))
            # Bottom right
            elif i == len(board)-1 and j == len(board[0])-1:
                if board[i-1][j] > val and board[i][j-1] > val:
                    low_points.append((i, j))
            # Check up, down, left and right
            elif board[i-1][j] > val and board[i][j-1] > val and board[i+1][j] > val and board[i][j+1] > val:
                low_points.append((i, j))
    print(len(low_points) + sum([board[p[0]][p[1]] for p in low_points]))
    return low_points


def get_slopes(curr, board):
    slopes = []
    i = curr[0]
    j = curr[1]

    val = board[i][j]

    # Top left
    if i == 0 and j == 0:
        if board[i][j + 1] != 9:
            slopes.append((i, j+1))
        if board[i + 1][j] != 9:
            slopes.append((i+1, j))
    # Top
    elif i == 0 and j != len(board[0]) - 1:
        if board[i][j + 1] != 9:
            slopes.append((i, j + 1))
        if board[i + 1][j] != 9:
            slopes.append((i+1, j))
        if board[i][j - 1] != 9:
            slopes.append((i, j-1))
    # Top right
    elif i == 0 and j == len(board[0]) - 1:
        if board[i][j - 1] != 9:
            slopes.append((i, j - 1))
        if board[i + 1][j] != 9:
            slopes.append((i+1, j))
    # Left
    elif i != len(board) - 1 and j == 0:
        if board[i + 1][j] != 9:
            slopes.append((i+1, j))
        if board[i - 1][j] != 9:
            slopes.append((i-1, j))
        if board[i][j + 1] != 9:
            slopes.append((i, j+1))
    # Right
    elif i != len(board) - 1 and j == len(board[0]) - 1:
        if board[i + 1][j] != 9:
            slopes.append((i+1, j))
        if board[i - 1][j] != 9:
            slopes.append((i-1, j))
        if board[i][j - 1] != 9:
            slopes.append((i, j-1))
    # Bottom left
    elif i == len(board) - 1 and j == 0:
        if board[i - 1][j] != 9:
            slopes.append((i-1, j))
        if board[i][j + 1] != 9:
            slopes.append((i, j+1))
    # Bottom
    elif i == len(board) - 1 and j != len(board[0]) - 1:
        if board[i][j + 1] != 9:
            slopes.append((i, j + 1))
        if board[i][j - 1] != 9:
            slopes.append((i, j - 1))
        if board[i - 1][j] != 9:
            slopes.append((i-1, j))
    # Bottom right
    elif i == len(board) - 1 and j == len(board[0]) - 1:
        if board[i - 1][j] != 9:
            slopes.append((i-1, j))
        if board[i][j - 1] != 9:
            slopes.append((i, j-1))
    # Check up, down, left and right
    else:
        if board[i - 1][j] != 9:
            slopes.append((i-1, j))
        if board[i][j - 1] != 9:
            slopes.append((i, j - 1))
        if board[i + 1][j] != 9:
            slopes.append((i+1, j))
        if board[i][j + 1] != 9:
            slopes.append((i, j+1))

    return slopes


def part2(board):
    sizes = []
    low_points = part1(board)

    for point in low_points:
        to_visit = [point]
        visited = []
        while len(to_visit) > 0:
            curr = to_visit.pop()

            if curr not in visited:
                visited.append(curr)
                to_add = get_slopes(curr, board)

                for p in to_add:
                    if board[p[0]][p[1]] != 9:
                        to_visit.append(p)
        sizes.append(len(visited))
    sizes.sort()
    print(sizes[len(sizes)-1] * sizes[len(sizes)-2] * sizes[len(sizes)-3])
    pass


lines = open("input.txt").readlines();
matrix = []

for line in lines:
    to_append = [int(char) for char in line.rstrip()]
    matrix.append(to_append)
part2(matrix)