from math import floor

open_chars = ["(", "<", "{", "["]
closed_chars = [")", ">", "}", "]"]
scores = {")": 3, "]":57, "}":1197, ">":25137}
scores2 = {")":1, "]":2, "}":3, ">":4}


def part1(lines):
    global open_chars
    global closed_chars
    global scores

    ret = 0
    corrupted = False
    final_lines = []

    for line in lines:
        stack = []
        for char in line.rstrip():
            # Open parenthesis, just add it to the stack
            if char in open_chars:
                stack.append(closed_chars[open_chars.index(char)])
            # Closed parenthesis
            else:
                # Check if it corresponds to the last opened parenthesis
                if char == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    ret += scores[char]
                    corrupted = True
                    break
        if not corrupted:
            final_lines.append(line)

    print(ret)


def part2(lines):
    global open_chars
    global closed_chars
    global scores

    all_rets = []
    corrupted = False
    final_lines = []

    for line in lines:
        stack = []
        ret = 0
        corrupted = False
        for char in line.rstrip():
            # Open parenthesis, just add it to the stack
            if char in open_chars:
                stack.append(closed_chars[open_chars.index(char)])
            # Closed parenthesis
            else:
                # Check if it corresponds to the last opened parenthesis
                if char == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    corrupted = True
                    break
        if not corrupted:
            final_lines.append(line)
            stack.reverse()
            for i in stack:
                ret *= 5
                ret += scores2[i]
            all_rets.append(ret)

    all_rets.sort()
    print(all_rets[floor(len(all_rets) / 2)])


my_lines = open("input.txt", "r").readlines()
part1(my_lines)
part2(my_lines)
