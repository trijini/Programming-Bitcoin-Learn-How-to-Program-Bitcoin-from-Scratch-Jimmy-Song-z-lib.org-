#!/usr/bin/env python3

# Exercise 4

from io import BytesIO
from ecc import S256Point, Signature
from helper import encode_varint, hash256, int_to_little_endian
from script import Script
from tx import Tx, SIGHASH_ALL

hex_tx = '0100000001868278ed6ddfb6c1ed3ad5f8181eb0c7a385aa0836f01d5e4789e6bd304d87221a000000db00483045022100dc92655fe37036f47756db8102e0d7d5e28b3beb83a8fef4f5dc0559bddfb94e02205a36d4e4e6c7fcd16658c50783e00c341609977aed3ad00937bf4ee942a8993701483045022100da6bee3c93766232079a01639d07fa869598749729ae323eab8eef53577d611b02207bef15429dcadce2121ea07f233115c6f09034c0be68db99980b9a6c5e75402201475221022626e955ea6ea6d98850c994f9107b036b1334f18ca8830bfff1295d21cfdb702103b287eaf122eea69030a0e9feed096bed8045c8b98bec453e1ffac7fbdbd4bb7152aeffffffff04d3b11400000000001976a914904a49878c0adfc3aa05de7afad2cc15f483a56a88ac7f400900000000001976a914418327e3f3dda4cf5b9089325a4b95abdfa0334088ac722c0c00000000001976a914ba35042cfe9fc66fd35ac2224eebdafd1028ad2788acdc4ace020000000017a91474d691da1574e6b3c192ecfb52cc8984ee7b6c568700000000'
hex_sec = '03b287eaf122eea69030a0e9feed096bed8045c8b98bec453e1ffac7fbdbd4bb71'
hex_der = '3045022100da6bee3c93766232079a01639d07fa869598749729ae323eab8eef53577d611b02207bef15429dcadce2121ea07f233115c6f09034c0be68db99980b9a6c5e754022'
hex_redeem_script = '475221022626e955ea6ea6d98850c994f9107b036b1334f18ca8830bfff1295d21cfdb702103b287eaf122eea69030a0e9feed096bed8045c8b98bec453e1ffac7fbdbd4bb7152ae'
sec = bytes.fromhex(hex_sec)
der = bytes.fromhex(hex_der)
redeem_script = Script.parse(BytesIO(bytes.fromhex(hex_redeem_script)))
stream = BytesIO(bytes.fromhex(hex_tx))

# modify the transaction
tx_obj = Tx.parse(stream)
# start with version
s = b''
s += int_to_little_endian(tx_obj.version, 4)
# add number of inputs
s += encode_varint(len(tx_obj.tx_ins))
# modify the single TxIn to have the ScriptSig to be the RedeemScript
tx_obj.tx_ins[0].script_sig = redeem_script
s += tx_obj.tx_ins[0].serialize()
# add the number of outputs
s += encode_varint(len(tx_obj.tx_outs))
# add each output serialization
for out in tx_obj.tx_outs:
    s += out.serialize()
# add the locktime
s += int_to_little_endian(tx_obj.locktime, 4)
# add the SIGHASH_ALL
s += int_to_little_endian(SIGHASH_ALL, 4)
# hash256 the result
s256 = hash256(s)
# interpret as a Big-Endian number
z = int.from_bytes(s256, 'big')
# parse the S256Point
point = S256Point.parse(sec)
# parse the Signature
sig = Signature.parse(der)
# verify that the point, z and signature work
print(point.verify(z, sig))
print()
