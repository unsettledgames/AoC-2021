import copy
from copy import deepcopy

def part1(base, rules):
    counts = {}
    pairs = {}

    for char in base:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    for i in range(0, len(base)-1):
        if base[i] + base[i+1] not in pairs:
            pairs[base[i] + base[i+1]] = 1
        else:
            pairs[base[i] + base[i + 1]] += 1

    for i in range(0, 40):
        pairs_after = copy.deepcopy(pairs)

        for pair in pairs.keys():
            if pairs[pair] > 0:
                pairs_after[pair] -= pairs[pair]
                to_add = rules[pair]
                if to_add in counts:
                    counts[to_add] += pairs[pair]
                else:
                    counts[to_add] = pairs[pair]

                # Pair with previous
                new_pair = pair[0] + to_add
                if new_pair in pairs_after:
                    pairs_after[new_pair] += pairs[pair]
                else:
                    pairs_after[new_pair] = pairs[pair]

                # Pair with next
                new_pair = to_add + pair[1]
                if new_pair in pairs_after:
                    pairs_after[new_pair] += pairs[pair]
                else:
                    pairs_after[new_pair] = pairs[pair]

        pairs = copy.deepcopy(pairs_after)
        print("Count sum: " + str(sum([counts[key] for key in counts])))
        print(counts)

    my_min = 10000000000000000000000000000000000000000000000
    my_max = -1
    
    for letter in counts.keys():
        if counts[letter] > my_max:
            my_max = counts[letter]
        elif counts[letter] < my_min:
            my_min = counts[letter]
    print(my_max - my_min)


def part2(base, rules):
    pass


lines = open("input.txt").readlines()
first = ""
ruleset = {}
for i in range(0, len(lines)):
    if i == 0:
        first = lines[i].rstrip()
    elif lines[i].rstrip() != '':
        rule = lines[i].rstrip().split(" -> ")
        ruleset[rule[0]] = rule[1]

part1(first, ruleset)
