def printmat(mat):
    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            print(mat[i][j], end=" ")
        print("\n", end="\n")

def part1(mat):
    costs = []

    for i in range(0, len(mat)):
        to_append = []
        for j in range(0, len(mat[0])):
            to_append.append(0)
        costs.append(to_append)

    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            if i == 0 and j == 0:
                costs[i][j] = 0
            elif i == 0:
                costs[i][j] = costs[i][j-1] + mat[i][j]
            elif j == 0:
                costs[i][j] = costs[i-1][j] + mat[i][j]
            else:
                costs[i][j] = mat[i][j] + min(costs[i-1][j], costs[i][j-1])

    print(costs[len(mat)-1][len(mat[0])-1])

    pass


def part2(mat):
    dist = []
    for i in range(0, len(mat)*5):
    #         to_append = []
    #         for j in range(0, len(mat)*5):
    #             to_append.append(0)
    #         costs.append(to_append)

# def part2(mat):
#     costs = []
#
#     for i in range(0, len(mat)*5):
#         to_append = []
#         for j in range(0, len(mat)*5):
#             to_append.append(0)
#         costs.append(to_append)
#
#     for i in range(0, len(mat)*5):
#         for j in range(0, len(mat)*5):
#             mat_val = (mat[i%len(mat)][j%len(mat)] + int(i / len(mat)) + int(j / len(mat)))
#             if mat_val > 9:
#                 mat_val = mat_val % 9
#             if i == 0 and j == 0:
#                 costs[i][j] = 0
#             elif i == 0:
#                 costs[i][j] = costs[i][j - 1] + mat_val
#             elif j == 0:
#                 costs[i][j] = costs[i - 1][j] + mat_val
#             else:
#                 costs[i][j] = mat_val + min(costs[i - 1][j], costs[i][j - 1])
#
#     print(costs[len(costs) - 1][len(costs) - 1])
#
#     pass


matrix = []
lines = open("input.txt", "r").readlines()
for line in lines:
    to_append = []
    matrix.append([int(line[i]) for i in range(0, len(line.rstrip()))])
part1(matrix)
part2(matrix)