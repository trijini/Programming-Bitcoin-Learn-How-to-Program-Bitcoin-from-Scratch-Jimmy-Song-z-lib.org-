#!/usr/bin/env python3

from importlib import reload
from helper import run
import network

from block import GENESIS_BLOCK
from helper import calculate_new_bits
from network import (
    NetworkEnvelope,
    VersionMessage,
)
from io import BytesIO

run(network.VersionMessageTest('test_serialize'))