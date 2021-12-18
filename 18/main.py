import math


class SnailNode:
    def __init__(self, string):
        self.string = string
        self.left = None
        self.right = None
        self.parent = None
        self.is_left = None

        if string.startswith("["):
            self.val = -1
            self.gen_tree(string)
        else:
            self.val = int(string)

    def get_pair_end(self, string):
        n_open = 0
        for i in range(0, len(string)):
            if string[i] == "[":
                n_open += 1
            elif string[i] == "]":
                n_open -= 1
            if n_open == 0:
                if i == 0:
                    return -1
                return i+1
        return -1

    def gen_tree(self, string):
        # Pair: parse left and right
        string = string[1:len(string)-1]
        pair_end = self.get_pair_end(string)
        self.val = -1

        if pair_end == -1:
            pair_end = string.find(",")
        self.left = SnailNode(string[0:pair_end])
        self.left.parent = self
        self.left.is_left = True

        self.right = SnailNode(string[pair_end+1:len(string)])
        self.right.parent = self
        self.right.is_left = False

    def add_left(self, val, child):
        if self.left != child and self.left.val != -1:
            self.left.val += val
            return True
        elif not self.left.contains(child) or self.parent is None:
            return self.left.add_left_inner(val, child)
        elif self.parent is not None:
            return self.parent.add_left(val, child)
        else:
            return False

    def add_left_inner(self, val, child):
        if self.val != -1:
            return False
        elif self.right.val != -1 and self.right != child and not self.left.contains(child):
            self.right.val += val
            return True
        elif self != child and not self.left.contains(child):
            return self.right.add_left_inner(val, child)
        else:
            return False

    def add_right(self, val, child):
        if self.right != child and self.right.val != -1:
            self.right.val += val
            return True
        elif not self.right.contains(child) or self.parent is None:
            return self.right.add_right_inner(val, child)
        elif self.parent is not None:
            return self.parent.add_right(val, child)
        else:
            return False

    def add_right_inner(self, val, child):
        if self.val != -1:
            return False
        elif self.left.val != -1 and self.left != child and not self.right.contains(child):
            self.left.val += val
            return True
        elif self != child and not self.right.contains(child):
            return self.left.add_right_inner(val, child)
        else:
            return False

    def contains(self, node):
        if self == node:
            return True
        elif self.val == -1:
            return self.right.contains(node) or self.left.contains(node)
        else:
            return False

    def explode(self, level=0):
        ret = False
        if self.right.val != -1 and self.left.val != -1 and level > 3:
            # Save values
            left = self.left.val
            right = self.right.val

            # Take left value, add it to the first on the left
            added_left = self.parent.add_left(left, self)

            # Take right value, add it to the firs on the right
            added_right = self.parent.add_right(right, self)

            # The top level node now has a 0
            if self.is_left:
                self.parent.left = SnailNode("0")
                self.parent.left.is_left = True
                self.parent.left.parent = self.parent
            else:
                self.parent.right = SnailNode("0")
                self.parent.right.is_left = False
                self.parent.right.parent = self.parent

            return added_right or added_left
        else:
            if self.left.val == -1:
                ret = self.left.explode(level + 1)
            else:
                ret = False

            if not ret and self.right.val == -1:
                return self.right.explode(level + 1)
            return ret

    def split(self):
        if self.val >= 10:
            self.left = SnailNode(str(math.floor(self.val / 2)))
            self.left.parent = self
            self.left.is_left = True

            self.right = SnailNode(str(math.ceil(self.val / 2)))
            self.right.parent = self
            self.right.is_left = False

            self.val = -1
            return True
        elif self.val != -1:
            return False
        else:
            return self.left.split() or self.right.split()

    def print_tree(self):
        if self.val == -1:
            print("[", end="")

            self.left.print_tree()
            print(",", end="")
            self.right.print_tree()

            print("]", end="")
        else:
            print(str(self.val), end="")

    def get_string(self):
        ret = ""
        if self.val == -1:
            ret += "["

            ret += self.left.get_string()
            ret += ","
            ret += self.right.get_string()

            ret += "]"
        else:
            ret += str(self.val)
        return ret

    def get_magnitude(self):
        if self.val != -1:
            return self.val
        else:
            return 3 * self.left.get_magnitude() + 2 * self.right.get_magnitude()


def part1(roots):
    new_tree = roots[0]
    for i in range(1, len(roots)):
        new_tree = SnailNode("[" + new_tree.get_string() + "," + roots[i].get_string() + "]")
        exploded = False
        splitted = True

        while exploded or splitted:
            exploded = new_tree.explode()
            if not exploded:
                splitted = new_tree.split()
    new_tree.print_tree()
    print()
    print(new_tree.get_magnitude())


def part2(roots):
    max_mag = -1

    for i in range(len(roots)):
        for j in range(len(roots)):
            if i != j:
                new_tree = SnailNode("[" + roots[i].get_string() + "," + roots[j].get_string() + "]")

                exploded = False
                splitted = True

                while exploded or splitted:
                    exploded = new_tree.explode()
                    if not exploded:
                        splitted = new_tree.split()

                curr_mag = new_tree.get_magnitude()

                if curr_mag > max_mag:
                    max_mag = curr_mag
    print(max_mag)
    pass


lines = open("input.txt", "r").readlines()
trees = []
for line in lines:
    trees.append(SnailNode(line.rstrip()))

part1(trees)
part2(trees)
