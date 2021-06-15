
class InvalidValue(Exception):
    def __init__(self, expression, message):
        self.expression = message
        self.message = message


def generate_white_keys(bit, key):
    # print('\nWHITE KEY GEN STARTS HERE\nPARAMS :: BIT :: KEY :: ', bit, key, '\n')
    ikey = int(key, 16)
    k = []
    wk = []
    # number of subkeys to be genrated
    sbit = int(bit / 16)

    #key as string
    skey = str(key)

    # key_binary = str(bin(int(key, 16))[2:]).zfill(bit)
    # print('KEY IN ASCII :::  ', len(key_binary), key_binary, type(key_binary))


    k2 = []

    # for i in range(sbit):
    #     k.append((ikey >> (2 * (sbit - i - 1))) & 0x0000ffff)

    #split the key into subkeys
    for i in range(len(skey), 0, -4):
        n1 = i
        n2 = i-4
        sub = skey[n2:n1]
        # print(i, '\t', n2, n1, skey[n2:n1], len(skey[n2:n1]))
        #print(hex(int(sub, 2)))
        k2.append(sub)

    # print('AFTER K :: ', k)
    k2.reverse()


    #convert strings to hex
    for i in k2:
        hex_int = int(i, 16)
        hexx = hex(hex_int)
        k.append(hexx)

    # print('AFTER K2 :: ', k2, k)

    if bit == 80:
        wk.append(k2[0][:2] + k2[1][2:])
        wk.append(k2[1][:2] + k2[0][2:])
        wk.append(k2[4][:2] + k2[3][2:])
        wk.append(k2[3][:2] + k2[4][2:])

    elif bit == 128:
        wk.append(k2[0][:2] + k2[1][2:])
        wk.append(k2[1][:2] + k2[0][2:])
        wk.append(k2[4][:2] + k2[7][2:])
        wk.append(k2[7][:2] + k2[4][2:])

    else:
        raise InvalidValue('bit=' + str(bit), 'The value of bit can be 80 or 128')

    # print('WHITE KEYS GENNED :: ', wk)

    return wk




def generate_round_keys(bit, key):
    print('\ROUND KEY GEN STARTS HERE\nPARAMS :: BIT :: KEY :: ', bit, key, '\n')
    ikey = int(key, 16)
    skey = str(key)
    k = []
    rk = []
    sbit = int(bit / 16)

    # for i in range(sbit):
    #     k.append((ikey >> (16 * (sbit - i - 1))) & 0x0000ffff)

    k2 = []
    # split the key into subkeys
    for i in range(len(skey), 0, -4):
        n1 = i
        n2 = i - 4
        sub = skey[n2:n1]
        k2.append(sub)

    k2.reverse()
    print('SUB KEYS ::: ', k2)

    _constant_value_80(2)

    # if bit == 80:
    #     for i in range(25):
    #         con2i = (_constant_value_80(i) & 0xffff0000) >> 16
    #         con2i1 = (_constant_value_80(i) & 0x0000ffff)
    #         if i % 5 == 2 or i % 5 == 0:
    #             rk.append(con2i ^ k[2])
    #             rk.append(con2i1 ^ k[3])
    #         elif i % 5 == 1 or i % 5 == 4:
    #             rk.append(con2i ^ k[0])
    #             rk.append(con2i1 ^ k[1])
    #         elif i % 5 == 3:
    #             rk.append(con2i ^ k[4])
    #             rk.append(con2i1 ^ k[4])
    # elif bit == 128:
    #     for i in range(62):
    #         if (i + 2) % 8 == 0:
    #             tmp = k
    #             k[0] = tmp[2]
    #             k[2] = tmp[6]
    #             k[3] = tmp[7]
    #             k[4] = tmp[0]
    #             k[5] = tmp[3]
    #             k[6] = tmp[4]
    #             k[7] = tmp[5]
    #         rk.append(k[(i + 2) % 8] ^ _constant_value_128(i))
    # else:
    #     raise InvalidValue('bit=' + str(bit), 'The value of bit can be 80 or 128')

    return rk


def _constant_value_80(i):

        cnn = "0f1e2d3c"
        ci1 = str(bin(i+1)[2:].zfill(5))
        c0 = str(bin(0)[2:].zfill(5))
        #convert to binary string
        c = ci1 + c0 + ci1 + "00" + ci1 + c0 + ci1
        c_hex = hex(int(c, 2))

        a = int(c_hex[2:], 16)
        b = int(cnn, 16)
        x = a^b
        con = bin(x)[2:].zfill(32)
        # print('HERE :: ', con, len(con))
        return con


def _constant_value_128(i):
        ci1 = i + 1
        con = 0
        con |= (((ci1 << 27) | (0 << 22) | (ci1 << 17) | (0 << 15) | (ci1 << 10) | (0 << 5) | (ci1)) ^ 0x6547a98b)
        return con