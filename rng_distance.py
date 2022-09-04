#!/usr/bin/python3
"""Determine the distance between two seeds

./rng_distance.py -s 0xC88F4F11 -f 0x765C83BB
Distance: 10
"""


import argparse
import sys

parser = argparse.ArgumentParser(description='DTM splitter used for AGDQ 2023')
parser.add_argument('--start', '-s', type=str, help='RNG seed start', default=0)
parser.add_argument('--finish', '-f', type=str, help='RNG seed finish', default=0)
args = parser.parse_args()

# RNG state is 16 bits for frame index plus
seed = int(args.start, 16)
final_seed = int(args.finish, 16)

#Gets inlined in both functions
#This one is egregious because it ends up being called twice in each
def get_seed():
    global seed
    return seed

#Gets inlined in both functions
#Uses a Linear Congruential Generator with a = 214013, c = 2531011, m = 2**32
#Has a period of 2**32 which is optimal considering the modulus
def next_seed():
    global seed
    seed = ((seed * 214013) + 2531011) % 2**32

#@80380580
#Returns a value between 0 and max_val-1
def get_random_int(max_val):
    next_seed()
    top_bits = get_seed() // 2**16
    return (max_val * top_bits) // 2**16

#@80380528
#Returns an evenly spaced value between 0 and 65535/65536
def get_random_float():
    next_seed()
    top_bits = get_seed() // 2**16
    return top_bits / 65536


i = 0
while True:
    if seed == final_seed:
        print("Distance:", i)
        sys.exit(0)
    next_seed()
    i += 1
