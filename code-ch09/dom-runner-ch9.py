#!/usr/bin/env python3

import io
from block import Block
from helper import target_to_bits, TWO_WEEKS

block1_hex = '000000203471101bbda3fe307664b3283a9ef0e97d9a38a7eacd88000000\
00000000000010c8aba8479bbaa5e0848152fd3c2289ca50e1c3e58c9a4faaafbdf5803c5448dd\
b845597e8b0118e43a81d3'
block2_hex = '02000020f1472d9db4b563c35f97c428ac903f23b7fc055d1cfc26000000\
000000000000b3f449fcbe1bc4cfbcb8283a0d2c037f961a3fdf2b8bedc144973735eea707e126\
4258597e8b0118e5f00474'
# parse both blocks
first_block = Block.parse(io.BytesIO(bytes.fromhex(block1_hex)))
last_block = Block.parse(io.BytesIO(bytes.fromhex(block2_hex)))
print()
# get the time differential
# if the differential > 8 weeks, set to 8 weeks
time_differential = last_block.timestamp - first_block.timestamp
if time_differential > TWO_WEEKS * 4:
    time_differential = TWO_WEEKS * 4
# if the differential < 1/2 week, set to 1/2 week
if time_differential < TWO_WEEKS // 4:
    time_differential = TWO_WEEKS // 4
# new target is last target * differential / 2 weeks
new_target = last_block.target() * time_differential // TWO_WEEKS
#new_target = time_differential * last_block.target() // TWO_WEEKS
# convert new target to bits
new_bits = target_to_bits(new_target)
print(f'New target to bits:\n{new_bits}')
# print the new bits hex
print(new_bits.hex())
print()
print()
print('Jimmy')

block1_hex = '000000203471101bbda3fe307664b3283a9ef0e97d9a38a7eacd88000000\
00000000000010c8aba8479bbaa5e0848152fd3c2289ca50e1c3e58c9a4faaafbdf5803c5448dd\
b845597e8b0118e43a81d3'
block2_hex = '02000020f1472d9db4b563c35f97c428ac903f23b7fc055d1cfc26000000\
000000000000b3f449fcbe1bc4cfbcb8283a0d2c037f961a3fdf2b8bedc144973735eea707e126\
4258597e8b0118e5f00474'
last_block = Block.parse(io.BytesIO(bytes.fromhex(block1_hex)))
first_block = Block.parse(io.BytesIO(bytes.fromhex(block2_hex)))
time_differential = last_block.timestamp - first_block.timestamp
if time_differential > TWO_WEEKS * 4:
    time_differential = TWO_WEEKS * 4
if time_differential < TWO_WEEKS // 4:
    time_differential = TWO_WEEKS // 4
new_target = last_block.target() * time_differential // TWO_WEEKS
new_bits = target_to_bits(new_target)
print(new_bits.hex())
print('hey')