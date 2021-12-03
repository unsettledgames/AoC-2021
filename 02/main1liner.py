lines = open("input.txt", "r").readlines()
print(sum([int(line[8:]) for line in lines if "forward" in line]) * (sum([int(line[5:]) for line in lines if "down" in line]) - sum([int(line[3:]) for line in lines if "up" in line])))
