# 0: 6 segments, top, topright, bottomright, bottom, bottomleft, topleft
# 1: 2 segments, topright, bottomright
# 2: 5 segments, top, topright, center, bottomleft, bottom
# 3: 5 segments, top, topright, center, bottomright, bottom
# 4: 4 segments, topleft, center, topright, bottomright
# 5: 5 segments, top, topleft, center, bottomright, bottom
# 6: 6 segments, top, topleft, center, bottomright, bottomleft, bottom
# 7: 3 segments, top, topleft, bottomleft
# 8: 7 segments, all of them
# 9: 6 segments, top, topright, topleft, center, bottomright, bottom

# 1, 4, 7 and 8 are unique

ciphers = [["top", "topright", "bottomright", "bottom", "bottomleft", "topleft"],
               ["topright", "bottomright"],
               ["top", "topright", "center", "bottomleft", "bottom"],
               ["top", "topright", "center", "bottomright", "bottom"],
               ["topleft", "center", "topright", "bottomright"],
               ["top", "topleft", "center", "bottomright", "bottom"],
               ["top", "topleft", "center", "bottomright", "bottomleft", "bottom"],
               ["top", "topleft", "bottomleft"],
               ["top", "topleft", "bottomleft", "topright", "bottomright", "top", "bottom"],
               ["top", "topright", "topleft", "center", "bottomright", "bottom"]]
numbers = {}
associations = {}
candidate_associations = {}

def part1(lines):
    ret = 0

    for line in lines:
        sections = line.split(" | ")
        second_digits = sections[1].split(" ")

        for digit in second_digits:
            digit_len = len(digit.rstrip())
            if digit_len == 2 or digit_len == 3 or digit_len == 4 or digit_len == 7:
                ret += 1

    print(ret)

    pass


def part2(lines):
    global numbers
    global associations
    ret = 0

    for line in lines:
        numbers = {}
        associations = {}

        original_line = line
        # Putting input and output on the same line
        line = line.rstrip().split(" | ")
        line = line[0] + " " + line[1]

        while len(numbers.keys()) < 10:
            for cipher in line.split(" "):
                create_number("".join(sorted(cipher.rstrip())))

        output = original_line.rstrip().split(" | ")[1]
        num = ""

        for cipher in output.split(" "):
            num += str(get_cipher("".join(sorted(cipher.rstrip()))))
        print(int(num))
        ret += int(num)

    print(ret)


def get_cipher(cipher):
    global numbers

    for i in numbers.keys():
        if numbers[i] == cipher:
            return i

    return 0


def create_number(cipher):
    global ciphers
    global numbers

    # 1
    if len(cipher) == 2:
        numbers[1] = "".join(sorted(cipher.rstrip()))
    # 7
    elif len(cipher) == 3:
        numbers[7] = "".join(sorted(cipher.rstrip()))
        if 1 in numbers.keys():
            for char in cipher:
                if char not in numbers[1]:
                    associations[char] = "top"
    # 4
    elif len(cipher) == 4:
        numbers[4] = "".join(sorted(cipher.rstrip()))
    # 2, 3 or 5
    elif len(cipher) == 5:
        found = False
        # 3 is the only one that has both topright and bottomright
        if 1 in numbers.keys():
            if str(numbers[1][0]) in cipher and str(numbers[1][1]) in cipher:
                numbers[3] = "".join(sorted(cipher.rstrip()))
                found = True
        if not found:
            if 4 in numbers.keys():
                missing = 0
                # 5 is a 4, but with the top part: the other character that 5 has but 4 doesn't is the top left
                for char in numbers[4]:
                    if char not in cipher:
                        missing += 1
                if missing == 1:
                    numbers[5] = "".join(sorted(cipher.rstrip()))
                else:
                    numbers[2] = "".join(sorted(cipher.rstrip()))
    # 0, 6 or 9
    elif len(cipher) == 6:
        # If I have 4 and 1, I can use them to derive other numbers
        if 4 in numbers.keys() and 1 in numbers.keys() and "top" in associations.values():
            all = True
            for char in numbers[4]:
                # If the middle character isn't in the current number, then the cipher is 0
                if char not in cipher and char not in numbers[1]:
                    numbers[0] = "".join(sorted(cipher.rstrip()))
                    associations[char] = "middle"
                    all = False
                elif char not in cipher and char in numbers[1]:
                    numbers[6] = "".join(sorted(cipher.rstrip()))
                    all = False
            if all:
                numbers[9] = "".join(sorted(cipher.rstrip()))

    elif len(cipher) == 7:
        numbers[8] = "".join(sorted(cipher.rstrip()))


my_lines = open("input.txt", "r").readlines()
part2(my_lines)
