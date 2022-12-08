#!/usr/bin/env python3

from io import BytesIO
from unittest import TestCase

import json
import requests
import tx
from ecc import PrivateKey
from helper import (
    encode_varint,
    hash256,
    int_to_little_endian,
    little_endian_to_int,
    read_varint,
    SIGHASH_ALL,
)
from script import Script

tx = tx.TxFetcher.fetch('46df1a9484d0a81d03ce0ee543ab6e1a23ed06175c104a178268fad381216c2b')
TestCase.assertTrue(tx.verify())
