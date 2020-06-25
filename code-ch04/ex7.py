def little_endian_to_int(h):
    b = bytes.fromhex(h)
    br = b[::-1]
    return int.from_bytes(br, "big")


def int_to_little_endian(n, length):
    print(f'arg:{n}')
    print(n.to_bytes(length, byteorder='little'))
    print(n.to_bytes(length, byteorder='big'))


int_to_little_endian(10011545, 8)
