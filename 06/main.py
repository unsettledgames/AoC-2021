fishes = {}

lines = list(map(int, str(open("input.txt", "r").read()).split(",")))
lines.sort()

while len(lines) > 0:
    fish = lines[0]
    count = lines.count(fish)

    fishes[fish] = count;
    lines = list(filter(lambda el : el != fish, lines))

for i in range(0, 256):
    new_fishes = fishes

    if 0 in fishes.keys():
        if 6 not in new_fishes.keys():
            new_fishes[7] = 0
        new_fishes[7] += fishes[0]
        if 8 not in new_fishes.keys():
            new_fishes[9] = 0
        new_fishes[9] += fishes[0]
        new_fishes[0] = 0

    for j in range(1, 10):
        if j in fishes.keys():
            if j-1 not in new_fishes.keys():
                new_fishes[j-1] = 0
            new_fishes[j-1] += fishes[j]
            new_fishes[j] = 0
        elif j in new_fishes.keys():
            del new_fishes[j]

    fishes = new_fishes

print(sum([fishes[k] for k in fishes.keys()]))