# from helper import (encode_varint, hash256, int_to_little_endian, little_endian_to_int, read_varint)
# import unittest
# from io import BytesIO
# from tx import TxIn
# from script import Script


# class Tx:
#     def __init__(self, version, tx_ins, tx_outs, locktime, testnet=False):
#         self.version = version
#         self.tx_ins = tx_ins  # <1>
#         self.tx_outs = tx_outs
#         self.locktime = locktime
#         self.testnet = testnet  # <2>
#
#     def __repr__(self):
#         tx_ins = ''
#         for tx_in in self.tx_ins:
#             tx_ins += tx_in.__repr__() + '\n'
#         tx_outs = ''
#         for tx_out in self.tx_outs:
#             tx_outs += tx_out.__repr__() + '\n'
#         return 'tx: {}\nversion: {}\ntx_ins:\n{}tx_outs:\n{}locktime: {}'.format(
#             self.id(),
#             self.version,
#             tx_ins,
#             tx_outs,
#             self.locktime,
#         )
#
#     def id(self):  # <3>
#         '''Human-readable hexadecimal of the transaction hash'''
#         return self.hash().hex()
#
#     def hash(self):  # <4>
#         '''Binary hash of the legacy serialization'''
#         return hash256(self.serialize())[::-1]
#     # end::source1[]
#
#     @classmethod
#     def parse(cls, s, testnet=False):


#
#
# class TestStringMethods(unittest.TestCase):
#     def test_parse_inputs(self):
#         raw_tx = bytes.fromhex(
#             '0100000001813f79011acb80925dfe69b3def355fe914bd1d96a3f5f71bf8303c6a989c7d1000000006b483045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031ccfcf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9c8e10615bed01210349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e213bf016b278afeffffff02a135ef01000000001976a914bc3b654dca7e56b04dca18f2566cdaf02e8d9ada88ac99c39800000000001976a9141c4bc762dd5423e332166702cb75f40df79fea1288ac19430600')
#         stream = BytesIO(raw_tx)
#         tx = Tx.parse(stream)
#         self.assertEqual(len(tx.tx_ins), 1)
#         want = bytes.fromhex('d1c789a9c60383bf715f3f6ad9d14b91fe55f3deb369fe5d9280cb1a01793f81')
#         self.assertEqual(tx.tx_ins[0].prev_tx, want)
#         self.assertEqual(tx.tx_ins[0].prev_index, 0)
#         want = bytes.fromhex(
#             '6b483045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031ccfcf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9c8e10615bed01210349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e213bf016b278a')
#         self.assertEqual(tx.tx_ins[0].script_sig.serialize(), want)
#         self.assertEqual(tx.tx_ins[0].sequence, 0xfffffffe)
#
# if __name__ == '__main__':
#     unittest.main()


from importlib import reload
from helper import run
import ecc
import helper
import script
import tx

raw_tx = bytes.fromhex()

