import functools;

tot = 1;
lines = open("input.txt","r").readlines()

for i in range(3, len(lines) - 1):
    prev = int(lines[i-1]) + int(lines[i-2]) + int(lines[i-3])
    curr = int(lines[i]) + int(lines[i-1]) + int(lines[i-2])

    if curr > prev:
        tot += 1

print(tot)
