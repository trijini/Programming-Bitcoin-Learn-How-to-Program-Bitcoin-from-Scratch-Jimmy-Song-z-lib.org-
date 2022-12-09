#!/usr/bin/env python3

from importlib import reload
from helper import run
import block
import ecc
import helper
import script
import tx


reload(tx)
run(tx.TxTest("test_coinbase_height"))