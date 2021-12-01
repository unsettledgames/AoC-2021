import functools;

tot = 1;
lines = open("input.txt","r").readlines()

for i in range(1, len(lines) - 1):
    prev = int(lines[i-1])
    curr = int(lines[i])

    if curr > prev:
        tot += 1

print(tot)
