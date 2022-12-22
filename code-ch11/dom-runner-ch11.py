#!/usr/bin/env python3

from importlib import reload
from helper import run
import block
import ecc
import helper
import network
import merkleblock
import script
import tx

run(merkleblock.MerkleBlockTest('test_parse'))
