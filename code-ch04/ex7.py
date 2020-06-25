def little_endian_to_int(h):
    reversed = ''
    print("byesfromhex")
    print(type(bytes.fromhex(h)))
    print(list(bytes.fromhex(h)).reverse())
    #
    # print(h[len(h)-1])
    # for i in range(len(h), 0, -2):
    #     reversed += h[i-2]+h[i-1]
    #
    # print('reversed'+ reversed)
    #
    # return (int(reversed, 16))

little_endian_to_int('99c3980000000000')