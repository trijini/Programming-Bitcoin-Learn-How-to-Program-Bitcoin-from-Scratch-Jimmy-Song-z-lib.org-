#!/usr/bin/env python3
from importlib import reload
from helper import run
from unittest import TestCase
import ecc
import helper
import tx
import script

import op


run(tx.TxTest("test_verify_p2pkh"))
