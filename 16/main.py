class Packet:
    def __init__(self, ver, pack_type, sub_packets):
        self.ver = ver
        self.pack_type = pack_type
        self.sub_packets = sub_packets


def parse_packet(pack):
    pack_len = 6
    # Get version
    ver = pack[0:3]
    # Get type
    pack_type = pack[3:6]
    type_dec = int(pack_type, 2)
    sub_packs = []

    if type_dec != 4:
        if pack[6] == "0":
            pack_len += 16
            tot_len = int(pack[7:22], 2)
            # add packet version and length
            prev_idx = 22
            curr_idx = 25

            pack_len += 3
            # Get subpackets
            while tot_len > 0:
                if int(pack[prev_idx:prev_idx+3], 2) == 4:
                    if pack[curr_idx] == '0':
                        curr_idx += 5
                        pack_len += 5
                        sub_packs.append(parse_packet(pack[prev_idx:curr_idx]))

                        tot_len -= (curr_idx - prev_idx)
                        prev_idx = curr_idx
                        curr_idx += 7
                        pack_len += 7
                    else:
                        curr_idx += 5
                        pack_len += 5
                else:
                    ret = parse_packet(pack[prev_idx:len(pack)])
                    sub_packs.append(ret[1])
                    tot_len -= ret[0]
                    pack_len += ret[0]
        else:
            n_packets = int(pack[7:18], 2)
            prev_idx = 18
            curr_idx = 24
            i = 0

            while i < n_packets:
                if int(pack[prev_idx:prev_idx+3], 2) == 4:
                    if n_packets == 1:
                        sub_packs.append(parse_packet(pack[prev_idx:len(pack)]))
                        i += 1
                    elif pack[curr_idx] == '0':
                        curr_idx += 5
                        sub_packs.append(parse_packet(pack[prev_idx:curr_idx]))
                        prev_idx = curr_idx
                        curr_idx += 6

                        i += 1
                    else:
                        curr_idx += 5
                else:
                    ret = parse_packet(pack[prev_idx:len(pack)])
                    sub_packs.append(ret[1])
                    i += 1
    else:


    return Packet(ver, pack_type, sub_packs)

def sum_ver(pack):
    my_sum = int(pack.ver, 2)
    for i in pack.sub_packets:
        my_sum += sum_ver(i)
    return my_sum

def part1(bins):
    my_sum = 0

    for bs in bins:
        my_sum += sum_ver(parse_packet(bs))

    print(my_sum)


lines = open("input.txt", "r").readlines()
binaries = []

for line in lines:
    binaries.append(str(bin(int(line.rstrip(), 16))[2:].zfill(len(4 * line.rstrip()))))

part1(binaries)