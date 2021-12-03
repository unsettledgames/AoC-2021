lines = open("input.txt", "r").readlines()
depth = 0
horizontal = 0

for line in lines:
    if "forward" in line:
        horizontal += int(line[8:])
    else:
        depth += -int(line[3:]) if "up" in line else int(line[5:])

print(depth * horizontal)