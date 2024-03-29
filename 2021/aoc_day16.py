#! python

import sys
import numpy as np

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

OP_SUM = 0
OP_PROD = 1
OP_MIN = 2
OP_MAX = 3
OP_GT = 5
OP_LT = 6
OP_EQ = 7

OP_SYM = {
    OP_SUM: '+',
    OP_PROD: '*',
    OP_MIN: 'min',
    OP_MAX: 'max',
    OP_GT: '>',
    OP_LT: '<',
    OP_EQ: '==',
}

class packet(object):
    def __init__(self, ver=None, typ=None, data=None):
        self.ver = ver
        self.typ = typ
        self.data = data

    def value(self):
        if self.typ == TYP_LITERAL:
            val = self.data
        elif self.typ == OP_SUM:
            val = sum([pkt.value() for pkt in self.data])
        elif self.typ == OP_PROD:
            val = np.prod([pkt.value() for pkt in self.data])
        elif self.typ == OP_MIN:
            val = min([pkt.value() for pkt in self.data])
        elif self.typ == OP_MAX:
            val = max([pkt.value() for pkt in self.data])
        elif self.typ == OP_GT:
            val = 0
            if self.data[0].value() > self.data[1].value():
                val = 1
        elif self.typ == OP_LT:
            val = 0
            if self.data[0].value() < self.data[1].value():
                val = 1
        elif self.typ == OP_EQ:
            val = 0
            if self.data[0].value() == self.data[1].value():
                val = 1

        return val

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

    return val, loc - start

def parse(bits, num=None):
    num_pkts = 0
    total_bits = len(bits)
    bits_left = total_bits
    to_parse = bits
    parsed = 0
    pkts = []
    while bits_left > TYP_E and (num is None or num_pkts < num):
        loop_parsed = 0
        if all([b == '0' for b in to_parse]):
            break
        ver = int(to_parse[VER_S:VER_E], base=2)
        typ = int(to_parse[TYP_S:TYP_E], base=2)
        loop_parsed += HDR_LEN
        if typ == TYP_LITERAL:
            literal, lit_len = parse_literal_val(to_parse, LIT_START)
            pkt = packet(ver, typ, literal)
            print(f'found lit ver: {ver} val: {literal}')
            loop_parsed += lit_len
        else: # operator
            len_id = to_parse[LEN_ID]
            len_e = LEN_E[len_id]
            op_len = int(to_parse[LEN_S:len_e], base=2)
            pkt = packet(ver, typ)
            print(f'found op {typ} {OP_SYM[typ]} ver: {ver} lid: {len_id} len: {op_len}')
            s = len_e
            loop_parsed += len_e - LEN_ID
            if len_id == '0': # op_len is bits
                e = s + op_len
                pkt.data, _ = parse(to_parse[s:e])
                loop_parsed += op_len
            else:
                pkt.data, num_parsed = parse(to_parse[s:], op_len)
                loop_parsed += num_parsed
        num_pkts += 1
        if loop_parsed < len(to_parse):
            to_parse = to_parse[loop_parsed:]
        parsed += loop_parsed
        bits_left -= loop_parsed
        #print(f'l {loop_parsed} | t {parsed} | left {bits_left} of {total_bits} | {num_pkts} of {num}')
        pkts.append(pkt)
    return pkts, parsed

def calc_ver_sum(pkts):
    ver_sum = 0
    for pkt in pkts:
        ver_sum += pkt.ver
        if pkt.typ != TYP_LITERAL:
            ver_sum += calc_ver_sum(pkt.data)
    return ver_sum

def eval_pkts(pkts):
    vals = []
    for pkt in pkts:
        vals.append(pkt.value())
    return vals

if __name__ == '__main__':
    filename = 'aoc_day16_input.txt'

    if len(sys.argv) > 1:
        filename = sys.argv[1]

    with open(filename) as f:
        hex_data = f.read().strip()

    bit_list = ['{:04b}'.format(int(h, base=16)) for h in hex_data]
    bits = ''.join(bit_list)

    pkts, bits_parsed = parse(bits)
    ver_sum = calc_ver_sum(pkts)
    print(f'version sum {ver_sum}')

    vals = eval_pkts(pkts)
    print('BITS result: ' + ', '.join([str(v) for v in vals]))
