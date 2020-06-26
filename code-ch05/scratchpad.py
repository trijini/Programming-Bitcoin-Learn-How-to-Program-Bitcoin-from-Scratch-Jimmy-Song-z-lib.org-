from helper import (encode_varint, hash256, int_to_little_endian, little_endian_to_int, read_varint)
from io import BytesIO
from script import Script

class TxIn:
    def __init__(self, prev_tx, prev_index, script_sig=None, sequence=0xffffffff):
        self.prev_tx = prev_tx
        self.prev_index = prev_index
        if script_sig is None:  # <1>
            self.script_sig = Script()
        else:
            self.script_sig = script_sig
        self.sequence = sequence

    def __repr__(self):
        return '{}:{}'.format(
            self.prev_tx.hex(),
            self.prev_index,
        )
    # end::source2[]

    @classmethod
    def parse(cls, s):
        '''Takes a byte stream and parses the tx_input at the start
        return a TxIn object
        '''
        print('----- inside TxIn -----')
        # prev_tx is 32 bytes, little endian
        prev_tx = s.read(32)
        prev_tx = prev_tx[::-1]
        print(f'prev_tx:{prev_tx}')

        # prev_index is an integer in 4 bytes, little endian
        prev_index = s.read(4)
        print(f'prev_index:{little_endian_to_int(prev_index)}')
        # use Script.parse to get the ScriptSig

        script = Script.parse(s).serialize()
        print(f'script got: {script}')

        # sequence is an integer in 4 bytes, little-endian
        sequence = s.read(4)[::-1].hex()
        print(f'sequence:{sequence}')
        # return an instance of the class (see __init__ for args)
        return TxIn(prev_tx=prev_tx, prev_index=prev_index, script_sig=script, sequence=sequence)

    # tag::source5[]
    def serialize(self):
        '''Returns the byte serialization of the transaction input'''
        result = self.prev_tx[::-1]
        result += int_to_little_endian(self.prev_index, 4)
        result += self.script_sig.serialize()
        result += int_to_little_endian(self.sequence, 4)
        return result
    # end::source5[]

    # tag::source8[]
    def fetch_tx(self, testnet=False):
        return TxFetcher.fetch(self.prev_tx.hex(), testnet=testnet)

    def value(self, testnet=False):
        '''Get the output value by looking up the tx hash.
        Returns the amount in satoshi.
        '''
        tx = self.fetch_tx(testnet=testnet)
        return tx.tx_outs[self.prev_index].amount

    def script_pubkey(self, testnet=False):
        '''Get the ScriptPubKey by looking up the tx hash.
        Returns a Script object.
        '''
        tx = self.fetch_tx(testnet=testnet)
        return tx.tx_outs[self.prev_index].script_pubkey
    # end::source8[]


class Tx:
    def __init__(self, version, tx_ins, tx_outs, locktime, testnet=False):
        self.version = version
        self.tx_ins = tx_ins  # <1>
        self.tx_outs = tx_outs
        self.locktime = locktime
        self.testnet = testnet  # <2>

    def __repr__(self):
        tx_ins = ''
        for tx_in in self.tx_ins:
            tx_ins += tx_in.__repr__() + '\n'
        tx_outs = ''
        for tx_out in self.tx_outs:
            tx_outs += tx_out.__repr__() + '\n'
        return 'tx: {}\nversion: {}\ntx_ins:\n{}tx_outs:\n{}locktime: {}'.format(
            self.id(),
            self.version,
            tx_ins,
            tx_outs,
            self.locktime,
        )

    def id(self):  # <3>
        '''Human-readable hexadecimal of the transaction hash'''
        return self.hash().hex()

    def hash(self):  # <4>
        '''Binary hash of the legacy serialization'''
        return hash256(self.serialize())[::-1]
    # end::source1[]

    @classmethod
    def parse(cls, s, testnet=False):
        '''Takes a byte stream and parses the transaction at the start
        return a Tx object
        '''
        # s.read(n) will return n bytes
        print('***********')
        # version is an integer in 4 bytes, little-endian
        version = s.read(4)
        # num_inputs is a varint, use read_varint(s)
        num_in = read_varint(s)

        # parse num_inputs number of TxIns
        tx_ins = TxIn.parse(s)


        # TODO: Complete below
        # num_outputs is a varint, use read_varint(s)
        # parse num_outputs number of TxOuts
        # locktime is an integer in 4 bytes, little-endian
        # return an instance of the class (see __init__ for args)


raw_tx = bytes.fromhex( '0100000001813f79011acb80925dfe69b3def355fe914bd1d96a3f5f71bf8303c6a989c7d1000000006b483045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031ccfcf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9c8e10615bed01210349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e213bf016b278afeffffff02a135ef01000000001976a914bc3b654dca7e56b04dca18f2566cdaf02e8d9ada88ac99c39800000000001976a9141c4bc762dd5423e332166702cb75f40df79fea1288ac19430600')
stream = BytesIO(raw_tx)
print(f'Original: {stream.getvalue()}')
tx = Tx.parse(stream)

# want = bytes.fromhex('d1c789a9c60383bf715f3f6ad9d14b91fe55f3deb369fe5d9280cb1a01793f81')
# print(f'want prev_tx:{want}')

# want_script = bytes.fromhex( '6b483045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031ccfcf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9c8e10615bed01210349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e213bf016b278a')
# print(f'want script:{want_script}')
