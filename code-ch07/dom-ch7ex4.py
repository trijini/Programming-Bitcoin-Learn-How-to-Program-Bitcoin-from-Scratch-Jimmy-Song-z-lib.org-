#!/usr/bin/env python3

from ecc import PrivateKey
from helper import decode_base58, SIGHASH_ALL
from script import p2pkh_script, Script
from tx import TxIn, TxOut, Tx, TxFetcher
import helper

pass1 = b'meoewmeow'
secret1 = helper.little_endian_to_int(helper.hash256(pass1))
priv1 = PrivateKey(secret1)
## PUBKEY: mtyMd6KL4UEhANPvZiFVUUkdz2rYg3kGkT
print(f'pass2:{pass1} secret2: {secret1}')
print(f'testnet address: {priv1.point.address(testnet=True)}')
tx_id1 = '9fc91f76d9125e1a2292fb69e55c097f030f27508ec965758c39bd82189c2729'
tx_id1_raw = bytes.fromhex(tx_id1)
utxo1 = TxFetcher.fetch(tx_id1, testnet=True)
prev_index1 = 0
tx_ins = []
tx_in = tx_ins.append(TxIn(tx_id1_raw, prev_index1))

tx_outs = []
utxo_amount = utxo1.tx_outs[prev_index1].amount
target_satoshis = int(utxo_amount * 0.95)
target_address = 'msbq2Y6X2rrDZGSkhZ7tpqcQ2PvmYo55hS'
h160 = decode_base58(target_address)
script_pubkey = p2pkh_script(h160)
tx_outs.append(TxOut(amount=target_satoshis, script_pubkey=script_pubkey))

tx_obj = Tx(1, tx_ins, tx_outs, 0, testnet=True)
print()
print(f'Input1 signed{tx_obj.sign_input(0, priv1)}')
print(f'tx serialized:{tx_obj.serialize().hex()}')


### Spending faucet coins, working
#pass2 = b'catocato'
#secret2 = helper.little_endian_to_int(helper.hash256(pass2))
#priv2 = PrivateKey(secret2)
## PUBKEY: mndE6UtaivGagKtNqedGCLP5SGXqSPFnYk
#print(f'pass2:{pass2} secret2: {secret2}')
#print(f'testnet address: {priv2.point.address(testnet=True)}')
#tx_id2 = '177cb536f241e24c2c22de1e568c3c928d397ccb8b5365a5ab92a7e3be34c25c'
#tx_id2_raw = bytes.fromhex(tx_id2)
#utxo2 = TxFetcher.fetch(tx_id2, testnet=True)
#prev_index2 = 0
#
#tx_ins = []
#tx_in = tx_ins.append(TxIn(tx_id2_raw, prev_index2))
#
#tx_outs = []
#utxo_amount = utxo2.tx_outs[prev_index2].amount
#target_satoshis = int(utxo_amount * 0.95)
#target_address = 'msbq2Y6X2rrDZGSkhZ7tpqcQ2PvmYo55hS'
#h160 = decode_base58(target_address)
#script_pubkey = p2pkh_script(h160)
#tx_outs.append(TxOut(amount=target_satoshis, script_pubkey=script_pubkey))
#
#tx_obj = Tx(1, tx_ins, tx_outs, 0, testnet=True)
#print()
#print(f'Input1 signed{tx_obj.sign_input(0, priv2)}')
##print(f'Input2 signed{tx_obj.sign_input(1, priv2)}')
#print(f'tx serialized:{tx_obj.serialize().hex()}')
