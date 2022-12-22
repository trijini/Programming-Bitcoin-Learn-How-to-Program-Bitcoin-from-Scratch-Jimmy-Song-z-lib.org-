#!/usr/bin/env python3

from importlib import reload
from helper import run
import block
import ecc
import helper
import network
import script
import tx

run(helper.HelperTest("test_merkle_parent"))