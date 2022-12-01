#!/usr/bin/env python3

from importlib import reload
from helper import run
import ecc
import helper
import op
import script
import tx

run(op.OpTest("test_op_checkmultisig"))