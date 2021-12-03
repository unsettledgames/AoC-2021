lines = open("input.txt", "r").readlines()
counts = {}
lineLen = len(lines[0]) - 1

for line in lines:
    for i in range(0, lineLen):
        if not str(i) in counts.keys():
            counts[str(i)] = 0
        if line[i] == '0':
            counts[str(i)] -= 1
        else:
            counts[str(i)] += 1

gamma = ""
for i in range(0, lineLen):
    gamma += str(1 if counts[str(i)] > 0 else 0)

epsilon = ""
for i in range(0, lineLen):
    epsilon += str(1 if counts[str(i)] < 0 else 0)

print(int(gamma, 2) * int(epsilon, 2))