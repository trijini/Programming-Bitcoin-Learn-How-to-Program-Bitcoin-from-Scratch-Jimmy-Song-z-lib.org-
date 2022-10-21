#!/usr/bin/python3

import binascii

secret = b'\xFF' * 32
print('Secret:{}'.format(secret))
secret_int = int.from_bytes(secret, byteorder='big')
print('Secret int:\t\t{}'.format(secret_int))
MAX_PRIV_KEY_INT = 2**256
REAL_MAX_PRIV_KEY_INT = 115792089237316195423570985008687907852837564279074904382605163141518161494336
REAL_MAX_PRIV_KEY_HEX = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140'
print('Real_max_priv_int:\t{}'.format(REAL_MAX_PRIV_KEY_INT))
print('Max num 2**256:\t\t{}'.format(MAX_PRIV_KEY_INT))
print('Real_max_priv_hex:\t{}'.format(REAL_MAX_PRIV_KEY_HEX))
print('Real_max_priv_hex len:\t{}'.format(len(REAL_MAX_PRIV_KEY_HEX)))

print()
secret = 'mishi-likes-apples-yum'
secret_encoded = secret.encode('utf-8')
print('secret:\t\t{}'.format(secret_encoded))
secret_hex = binascii.hexlify(secret.encode('utf8'))
print('b mishi secret bytes:\t\t{}'.format(secret_hex))
print('b mishi secret int.from_bytes:\t{}'.format(int.from_bytes(secret_encoded,'big')))


