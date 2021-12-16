import math


class Packet:
    def __init__(self, ver, pack_type, sub_packets):
        self.ver = ver
        self.pack_type = pack_type
        self.sub_packets = sub_packets
        self.val = -1

class PacketParser:
    def __init__(self, packet):
        self.packet = packet
        self.curr = 0
        self.start = 0
        self.pack_len = len(packet)
        self.length_type = 0

    def read_ver(self):
        ret = self.packet[self.curr : self.curr+3]
        self.curr += 3
        return ret

    def read_type(self):
        ret = self.packet[self.curr : self.curr + 3]
        self.curr += 3
        return ret

    def read_length_type(self):
        ret = self.packet[self.curr]
        self.curr += 1
        return ret

    def read_length(self):
        ret = self.packet[self.curr : self.curr + 15]
        self.curr += 15
        return ret

    def read_n_sub(self):
        ret = self.packet[self.curr : self.curr + 11]
        self.curr += 11
        return ret

    def read_next_packet(self):
        ret = Packet("", "", [])

        ret.ver = self.read_ver()
        ret.pack_type = self.read_type()

        if ret.pack_type == "100":
            literal = self.read_literal()
            ret.val = literal[0]
            return [self.curr, ret]
        else:
            l_type = self.read_length_type()
            if l_type == "0":
                length = int(self.read_length(), 2)

                parser = PacketParser(self.packet[self.curr:])
                start_length = length
                while length > 0:
                    next_pack = parser.read_next_packet()

                    ret.sub_packets.append(next_pack[1])
                    length = start_length - next_pack[0]
                self.curr += next_pack[0]
            else:
                n_packets = int(self.read_n_sub(), 2)
                for i in range(0, n_packets):
                    parser = PacketParser(self.packet[self.curr:])
                    next_pack = parser.read_next_packet()
                    self.curr += next_pack[0]
                    ret.sub_packets.append(next_pack[1])
        return [self.curr, ret]

    def read_literal(self):
        end = self.curr

        while self.packet[end] != "0":
            end += 5

        end += 5
        ret = self.packet[self.curr: end]
        length = end - self.curr
        self.curr = end

        ret_copy = ret
        for i in range(0, len(ret)):
            if i % 5 == 0:
                ret_copy = ret_copy[0:i - int(i/5)] + ret_copy[i + 1 - int(i/5):]

        return [ret_copy, length]


def sum_ver(pack):
    my_sum = int(pack.ver, 2)
    for i in pack.sub_packets:
        my_sum += sum_ver(i)
    return my_sum


def part1(bins):
    my_sum = 0

    for bs in bins:
        parser = PacketParser(bs)
        my_sum += sum_ver(parser.read_next_packet()[1])

    print(my_sum)


def part2(bins):
    for bs in bins:
        parser = PacketParser(bs)
        print(compute(parser.read_next_packet()[1]))


def compute(packet):
    if packet.pack_type == "000":
        sum = 0
        for i in packet.sub_packets:
            sum += compute(i)
        return sum
    elif packet.pack_type == "001":
        prod = 1
        for i in packet.sub_packets:
            prod *= compute(i)
        return prod
    elif packet.pack_type == "010":
        ret = math.inf
        for i in packet.sub_packets:
            ret = min(ret, compute(i))
        return ret
    elif packet.pack_type == "011":
        ret = -1
        for i in packet.sub_packets:
            ret = max(ret, compute(i))
        return ret
    elif packet.pack_type == "100":
        return int(packet.val, 2)
    elif packet.pack_type == "101":
        return compute(packet.sub_packets[0]) > compute(packet.sub_packets[1])
    elif packet.pack_type == "110":
        return compute(packet.sub_packets[0]) < compute(packet.sub_packets[1])
    elif packet.pack_type == "111":
        return compute(packet.sub_packets[0]) == compute(packet.sub_packets[1])


lines = open("input.txt", "r").readlines()
binaries = []

for line in lines:
    binaries.append(str(bin(int(line.rstrip(), 16))[2:].zfill(len(4 * line.rstrip()))))

part1(binaries)
part2(binaries)