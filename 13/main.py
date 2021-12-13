def count_dots(mat, size):
    ret = 0
    for i in range(0, size[1]):
        for j in range(0, size[0]):
            if mat[i][j] == "#":
                ret += 1
    print(ret)


def printmat(mat, size):
    for i in range(0, size[1]):
        for j in range(0, size[0]):
            print(mat[i][j], end="")
        print("\n", end="")


def part1(mat, fold, size):
    mat_bounds = [0, 0, size[0], size[1]]

    for f in fold:
        if f.startswith("y"):
            fold_idx = int(f.removeprefix("y"))
            # Fold bottom on top
            mat_bounds[3] = fold_idx
            for i in range(0, fold_idx):
                for j in range(0, mat_bounds[2]):
                    if mat[fold_idx - 1 - i][j] == ".":
                        mat[fold_idx - 1 - i][j] = mat[fold_idx + 1 + i][j]
        else:
            fold_idx = int(f.removeprefix("x"))
            # Fold left on right
            mat_bounds[0] = fold_idx + 1

            for i in range(0, mat_bounds[3]):
                k = 1
                for j in range(fold_idx + 1, mat_bounds[2]):
                    if mat[i][j] == ".":
                        mat[i][j] = mat[i][fold_idx - k]
                    k += 1

        for i in range(mat_bounds[1], mat_bounds[3]):
            for j in range(mat_bounds[0], mat_bounds[2]):
                mat[i - mat_bounds[1]][j - mat_bounds[0]] = mat[i][j]

        mat_bounds[2] -= mat_bounds[0]
        mat_bounds[3] -= mat_bounds[1]
        mat_bounds[0] = 0
        mat_bounds[1] = 0
    printmat(mat, [mat_bounds[2], mat_bounds[3]])
    pass


def part2(mat):
    pass


lines = open("input.txt", "r").readlines()
matrix = []
folds = []
mat_size = []
width = 0
height = 0

for line in lines:
    matrix.append(['.' for i in range(0, 1500)])

for line in lines:
    if line.startswith("fold"):
        line = line.removeprefix("fold along ")
        line = line.replace("=", "").rstrip()
        folds.append(line)
    elif line != "\n":
        coords = line.rstrip().split(",")
        matrix[int(coords[1])][int(coords[0])] = "#"
        if int(coords[1]) > width:
            width = int(coords[1])
        if int(coords[0]) > height:
            height = int(coords[0])

mat_size = [height+1, width+1]
part1(matrix, folds, mat_size)