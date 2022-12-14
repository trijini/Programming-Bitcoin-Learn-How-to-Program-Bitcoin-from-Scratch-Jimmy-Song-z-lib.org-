#!/usr/bin/env python3

import io

import helper
from helper import target_to_bits, TWO_WEEKS, run
# import everything and define a test runner function
from importlib import reload
import block
import ecc
import helper
import script
import tx

run(helper.HelperTest("test_calculate_new_bits"))