#!/usr/bin/env python3

from importlib import reload
from helper import run
import ecc
import helper
import op
import script
import tx

#tx = tx.TxFetcher.fetch('46df1a9484d0a81d03ce0ee543ab6e1a23ed06175c104a178268fad381216c2b')
#TestCase.assertTrue(tx.verify())

reload(tx)
run(tx.TxTest("test_verify_p2sh"))