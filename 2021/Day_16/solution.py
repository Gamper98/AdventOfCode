import os
from config.definitions import ROOT_DIR
import re
from collections import defaultdict
from math import prod

def read(text):
    with open(text, 'r') as f:
        data = f.read().rstrip('\n')
        packet = bin(int(data, 16))[2:].zfill(len(data) * 4)
        return packet

def decode_packet(packets, p_id, sub_packet):
    marker = 0
    packets[p_id]['version'] = sub_packet[marker: marker+3]
    marker += 3
    packets[p_id]['PacketTypeID'] = sub_packet[marker: marker+3]
    marker += 3
    if packets[p_id]['PacketTypeID'] != '100':
        packets[p_id]['lengthTypeID'] = sub_packet[marker]
        marker += 1
        if packets[p_id]['lengthTypeID'] == '1':
            packets[p_id]['length'] = sub_packet[marker: marker+11]
            marker += 11
        else:
            packets[p_id]['length'] = sub_packet[marker: marker+15]
            marker += 15
        count = 0
        p_remain = int(packets[p_id]['length'], 2)
        while True:
            if not re.search(r'[1]',sub_packet[marker:]) or p_remain == 0:
                return marker
            tmp = decode_packet(packets, str(p_id)+'.'+str(count), sub_packet[marker:])
            p_remain -= pow(tmp, packets[p_id]['lengthTypeID'] == '0')
            marker += tmp
            count += 1
    else:
        while True:
            is_end = sub_packet[marker]
            packets[p_id]['subpackets'].append(sub_packet[marker+1: marker+5])
            marker += 5
            if is_end == '0':
                return marker

def create_packet(packet_raw):
    packets = defaultdict(lambda: {
    'version': '', 
    'PacketTypeID': '', 
    'lengthTypeID': '',
    'length': '',
    'subpackets': []})
    decode_packet(packets, '0', packet_raw) 
    return packets

def solution_A(packet_raw):
    packets = create_packet(packet_raw)
    return sum([int(packet['version'], 2) for packet in packets.values()])

def calc_packet(packets, layer, idx):
    operators = {
        '000': sum,
        '001': prod,
        '010': min,
        '011': max,
        '100': lambda x: int(''.join(x), 2),
        '101': lambda x: x[0] > x[1],
        '110': lambda x: x[0] < x[1],
        '111': lambda x: x[0] == x[1]
    }
    if packets[layer]['PacketTypeID'] == '100':
        return 0, operators[packets[layer]['PacketTypeID']](packets[layer]['subpackets'])
    v = []
    keys = list(packets.keys())
    count = 0
    while idx + count < len(keys) and keys[idx + count].startswith(layer):
        r_count , num = calc_packet(packets, keys[idx + count], idx+1 + count)
        v.append(num)
        count += 1 + r_count
    return count, operators[packets[layer]['PacketTypeID']](v)
    
    
def solution_B(packet_raw):
    packets = create_packet(packet_raw)
    _, packet_value = calc_packet(packets, '0', 1)
    return packet_value

def main():
    packet = read(os.path.join(ROOT_DIR, '2021\Day_16\input', 'input.txt'))
    sol_A = solution_A(packet)
    sol_B = solution_B(packet)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()