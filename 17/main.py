
def strong_valid(pos, box):
    return pos[0] <= box[2] and pos[1] >= box[3]


def check_collision(pos, box):
    return box[0] <= pos[0] <= box[2] and box[1] >= pos[1] >= box[3]


def part1(box):
    curr_max = -1
    n_shoots = 0
    collided = False
    found = []

    for x in range(0, box[2]+1):
        for y in range(box[3], 1000):
            init_val = [x, y]
            start_vel = [x, y]
            start_point = [0, 0]
            throw_max = -1

            while strong_valid(start_point, box):
                start_point[0] += start_vel[0]
                start_point[1] += start_vel[1]

                throw_max = max(throw_max, start_point[1])

                start_vel[0] = max(start_vel[0] - 1, 0)
                start_vel[1] -= 1

                if check_collision(start_point, box):
                    collided = True
                    throw_max = max(throw_max, start_point[1])
            if collided:
                curr_max = max(curr_max, throw_max)
                collided = False
                if init_val not in found:
                    n_shoots += 1
                    found.append(init_val)

    print(curr_max)
    print(n_shoots)

line = open("input.txt", "r").readlines()[0].rstrip()
line = line.removeprefix("target area: x=")
coords = line.split(" ")

min_x = int(coords[0].split("..")[0])
max_x = int(coords[0].split("..")[1].removesuffix(","))

min_y = int(coords[1].split("..")[0].removeprefix("y="))
max_y = int(coords[1].split("..")[1])

bb = [min(min_x, max_x), max(min_y, max_y), max(min_x, max_x), min(min_y, max_y)]

part1(bb)
