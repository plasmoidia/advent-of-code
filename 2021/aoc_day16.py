#! python

import sys

VER_S = 0
VER_E = VER_S + 3
TYP_S = 3
TYP_E = TYP_S + 3
HDR_LEN = 3 + 3
LEN_ID = 6
LEN_S = 7
LEN_E = {'0': LEN_S+15, '1': LEN_S+11}

TYP_LITERAL = 4
LIT_START = 6
LIT_NIB_LEN = 5
LIT_LAST = '0'

class packet(object):
    def __init__(self, ver=None, typ=None, data=None):
        self.ver = ver
        self.typ = typ
        self.data = data

def parse_literal_val(bits, start=0):
    last = False
    loc = start
    val = 0

    while not last:
        nibble = bits[loc:loc+LIT_NIB_LEN]
        last = nibble[0] == LIT_LAST
        nibble = int(nibble[1:], base=2)
        val = val*16 + nibble
        loc += LIT_NIB_LEN

    return val, loc

def parse(bits, num=None):
    num_pkts = 0
    total_bits = len(bits)
    bits_left = total_bits
    to_parse = bits
    pkts = []
    while bits_left > TYP_E and (num is None or num_pkts < num):
        ver = int(to_parse[VER_S:VER_E], base=2)
        typ = int(to_parse[TYP_S:TYP_E], base=2)
        bits_left -= HDR_LEN
        if typ == TYP_LITERAL:
            literal, lit_len = parse_literal_val(bits, LIT_START)
            pkt = packet(ver, typ, literal)
            print(f'found lit ver: {ver} val: {literal}')
            bits_left -= lit_len
        else: # operator
            len_id = to_parse[LEN_ID]
            len_e = LEN_E[len_id]
            op_len = int(to_parse[LEN_S:len_e], base=2)
            pkt = packet(ver, typ)
            print(f'found op ver: {ver} lid: {len_id} len: {op_len}')
            s = len_e
            if len_id == '0': # op_len is bits
                e = s + op_len
                pkt.data, _ = parse(to_parse[s:e])
                bits_left -= op_len
            else:
                pkt.data, num_parsed = parse(to_parse[s:], op_len)
                bits_left -= num_parsed
        num_pkts += 1
        pkts.append(pkt)
    return pkts, total_bits - bits_left

if __name__ == '__main__':
    filename = 'aoc_day16_sample1.txt'

    if len(sys.argv) > 1:
        filename = sys.argv[1]

    with open(filename) as f:
        hex_data = f.read().strip()

    bit_list = ['{:04b}'.format(int(h, base=16)) for h in hex_data]
    bits = ''.join(bit_list)

    pkts, bits_parsed = parse(bits)
    print(pkts)
