def mostCommon(mylines, idx):
    ret = 0
    for line in mylines:
        if line[idx] == '0':
            ret -= 1
        else:
            ret += 1

    return 1 if ret >= 0 else 0

def getRating(type, mylines):
    currLines = mylines
    i = 0

    while len(currLines) != 1:
        starting = str(mostCommon(currLines, i))

        if type == "C" and starting == "0":
            starting = '1'
        elif type == "C" and starting == "1":
            starting = '0'

        postLines = []

        for line in currLines:
            if line[i] == starting:
                postLines.append(line)
        i += 1
        currLines = postLines

    return int(currLines[0], 2)


lines = open("input.txt", "r").readlines()
print(getRating("O", lines) * getRating("C", lines))


