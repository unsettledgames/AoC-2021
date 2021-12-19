import math
from ast import literal_eval as str_to_list

import numpy
import numpy as np
from numpy import sign

def rotations():
    """Generate all possible rotation functions"""
    vectors = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]
    vectors = list(map(np.array, vectors))
    for vi in vectors:
        for vj in vectors:
            if vi.dot(vj) == 0:
                vk = np.cross(vi, vj)
                yield lambda x: np.matmul(x, np.array([vi, vj, vk]))


def point_distance(a, b):
    return [abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2])]


def equal_distance(dista, distb):
    return dista[0] in distb and dista[1] in distb and dista[2] in distb


def compute_distances(scanner):
    ret = {}

    for i in range(len(scanner)):
        for j in range(len(scanner)):
            dist = point_distance(scanner[i], scanner[j])
            if dist[0] <= 1000 and dist[1] <= 1000 and dist[2] <= 1000 and str(dist) not in ret:
                ret[str(dist)] = [scanner[i], scanner[j]]

    return ret


def get_common_dists(dist1, dist2):
    ret = []

    for i in dist1:
        for j in dist2:
            if i != "[0, 0, 0]" and equal_distance(str_to_list(i), str_to_list(j)):
                ret.append([dist1[i], dist2[j]])

    return ret


def rotation_matrix_from_vectors(vec1, vec2):
    a, b = (vec1 / np.linalg.norm(vec1)).reshape(3), (vec2 / np.linalg.norm(vec2)).reshape(3)
    v = np.cross(a, b)
    c = np.dot(a, b)
    s = np.linalg.norm(v)
    kmat = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    rotation_matrix = np.eye(3) + kmat + kmat.dot(kmat) * ((1 - c) / (s ** 2))
    return rotation_matrix


def rotate(original, corresponding, scanner):
    if original == corresponding:
        return
    tmp = corresponding

    for rot in rotations():
        last_rot = rot
        tmp = rot(corresponding)
        print(numpy.cross(tmp, original))
        if (tmp == [605, -423, 415]).all():
            print("sas")
        if abs(numpy.cross(tmp, original) < 0.1).all():
            break

    rotated_corr = last_rot(corresponding)

    out = open("out.txt", "w")
    for i in range(len(scanner)):
        #vec = last_rot(np.array(scanner[i]))
        #scanner[i] = vec.tolist()
        if scanner[i] == corresponding:
            print("sas")
        for j in range(3):
            scanner[i][j] -= rotated_corr[j] + original[j]
            scanner[i][j] = int(scanner[i][j])
    for line in scanner:
        out.write(str(line) + "\n")


def part1(scanners):
    scannerIdx = 1
    while len(scanners) > 1:
        if scannerIdx == 0:
            scannerIdx += 1
            continue
        # Compute distances between points
        dist0 = compute_distances(scanners[0])
        disti = compute_distances(scanners[scannerIdx])

        # Find common distances (coord by coord) between a scanner and the next one
        common_dists = get_common_dists(dist0, disti)
        candidates = {}
        for i in range(len(common_dists)):
            candidateKey = str(common_dists[i][0][0])

            if candidateKey not in candidates:
                candidates[candidateKey] = []
            candidates[candidateKey].append(common_dists[i])

        j = 0

        while len(candidates) > 12:
            candidates = {k: v for k, v in candidates.items() if len(v) > j}
            j += 1

        # Find corresponding coords
        corresponding = {}

        if len(list(candidates.keys())) > 8:
            # Use the most accurate comparison to rotate the scanner
            most_accurate = {}
            most_acc_val = -1

            for i in candidates:
                possibles = {}

                for j in candidates[i]:
                    connection = str(j[1][0])
                    if connection not in possibles:
                        possibles[connection] = 0
                    possibles[connection] += 1

                max_val = -1
                max_conn = {}

                for j in possibles:
                    if possibles[j] > max_val:
                        max_val = possibles[j]
                        max_conn = j
                corresponding[i] = max_conn
                if max_val > most_acc_val:
                    most_acc_val = max_val
                    most_accurate = i

            # Edit all the points in the second scanner to be rotated correctly
            # Translate all the points in the second scanner to be relative to the first one
            rotate(str_to_list(most_accurate), str_to_list(corresponding[most_accurate]), scanners[scannerIdx])

            # Add the points of the second scanner to the first one
            for point in scanners[scannerIdx]:
                if point not in scanners[0]:
                    scanners[0].append(point)
                else:
                    print(point)
            scanners.remove(scanners[scannerIdx])
        else:
            scannerIdx = (scannerIdx + 1) % len(scanners)
    print(len(scanners[0]))

lines = open("input.txt", "r").readlines()
points = []
to_append = []
for line in lines:
    if line.startswith("--- scanner"):
        if to_append:
            points.append(to_append)
        to_append = []
    elif line.rstrip() != "":
        to_append.append(list(map(int, line.rstrip().split(","))))

part1(points)