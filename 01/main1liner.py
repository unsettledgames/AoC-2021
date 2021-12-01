from functools import reduce;
from numpy import sign;

print(sum([1 if y-x > 0 else 0 for (y,x) in zip(list(map(int, open("input.txt", "r").readlines()))[1:], list(map(int, open("input.txt", "r").readlines())))]))