import numpy as np


class InvalidValue(Exception):
    def __init__(self, expression, message):
        self.expression = message
        self.message = message


def split_bits(value, n):

    mask, parts = (1 << n) - 1, []
    print('MASK :: ', hex(mask), bin(mask))
    parts = []
    while value:
        parts.append(value & mask)
        # print('APPENDED VAL :: ', hex(value & mask))
        value >>= n
        # print('NEW VAL/SHIFTED :: ', hex(value))

    parts.reverse()
    # print('PARTS AFTER REVERSAL :: ', [hex(x) for x in parts])
    return parts


def generate_white_keys(bit, key):
    # print('GEN WHITE KEYS :: PAR4AMS ::: ', bit, key)
    ikey = int(key)
    k = []
    wk = []

    # print('ENTERING SPLITTER :: ', bit, key)
    k = split_bits(key, 16)
    # print('KEY SPLIT ::: ', [hex(x) for x in k])


    if bit == 80:
        wk.append((k[0] & 0xff00) | (k[1] & 0x00ff))
        wk.append((k[1] & 0xff00) | (k[0] & 0x00ff))
        wk.append((k[4] & 0xff00) | (k[3] & 0x00ff))
        wk.append((k[3] & 0xff00) | (k[4] & 0x00ff))
    elif bit == 128:
        wk.append((k[0] & 0xff00) | (k[1] & 0x00ff))
        wk.append((k[1] & 0xff00) | (k[0] & 0x00ff))
        wk.append((k[4] & 0xff00) | (k[7] & 0x00ff))
        wk.append((k[7] & 0xff00) | (k[4] & 0x00ff))
    else:
        raise InvalidValue('bit=' + str(bit), 'The value of bit can be 80 or 128')

    print('WHITE KEYS GENNED :: ', hex(key) , [hex(x) for x in wk])
    return wk




def generate_round_keys(bit, key):
    print('GEN ROUND KEYS :: PAR4AMS ::: ', bit, key)
    ikey = int(key)
    skey = str(key)
    k = []
    rk = []
    sbit = int(bit / 16)

    k = split_bits(key, 16)
    print('KEY SPLIT ::: ', [hex(x) for x in k])

    if bit == 80:
        r = 25
    elif bit == 128:
        r = 31

    rk = np.ones((2*r + 1), dtype=int)
    cons = np.ones((2*r + 1), dtype=int)
    print(rk.shape, cons.shape, type(cons), print(cons[30]))


    if bit == 80:
        for i in range(r-1):
            #generate constant
            l, r = get_contsant_values(i, bit)
            cons[2*i] = l
            cons[2*i + 1] = r
            # print('CON80 RK :: ', i, hex(l), hex(r), hex(cons[2*i]), hex(cons[2*i + 1]))

            if i % 5 == 2 or i % 5 == 0:
                z = cons[2*i] ^ k[2]
                rk[2*i] = z

                z = cons[2*i + 1] ^ k[3]
                rk[2*i + 1] = z

            elif i % 5 == 1 or i % 5 == 4:
                z = cons[2 * i] ^ k[0]
                rk[2 * i] = z

                z = cons[2 * i + 1] ^ k[1]
                rk[2 * i + 1] = z

            elif i % 5 == 3:
                z = cons[2 * i] ^ k[4]
                rk[2 * i] = z

                z = cons[2 * i + 1] ^ k[4]
                rk[2 * i + 1] = z

        print('DONE 80 RK GEN :: ')

    elif bit == 128:
        for i in range(2*r - 1):

            # generate constant
            con = _constant_value_128(i)
            # split con
            con2i_1 = con[16:32]
            con2i = con[0:16]
            con2i_1 = hex(int(con2i_1, 2))
            con2i = hex(int(con2i, 2))


            if (i + 2) % 8 == 0:
                tmp = k
                k[0] = tmp[2]
                k[2] = tmp[6]
                k[3] = tmp[7]
                k[4] = tmp[0]
                k[5] = tmp[3]
                k[6] = tmp[4]
                k[7] = tmp[5]


            indx = (i + 1) % 8

            a = int(k[indx], 16)
            b = int(con2i[2:], 16)

            x = a ^ b
            z = bin(x)[2:].zfill(16)

            rk[i] = z

    else:
        raise InvalidValue('bit=' + str(bit), 'The value of bit can be 80 or 128')

    # print('ROUND KEYS GENNED :: ', rk)
    return rk

def get_contsant_values(i, bit):
    cnn = 0x0f1e2d3c if bit==80 else 0x6547a98b
    ci_1 = (i + 1)
    cc = (ci_1 << 27) | (0 << 22) | (ci_1 << 17) | (0 << 15) | (ci_1 << 10) | (0 << 5) | (ci_1)
    cons = cc ^ cnn
    left = cons >> 16
    right = cons & 0xffff

    return (left, right)


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
    cnn = "6547a98b"
    ci1 = str(bin(i + 1)[2:].zfill(5))
    c0 = str(bin(0)[2:].zfill(5))
    # convert to binary string
    c = ci1 + c0 + ci1 + "00" + ci1 + c0 + ci1
    c_hex = hex(int(c, 2))

    a = int(c_hex[2:], 16)
    b = int(cnn, 16)
    x = a ^ b
    con = bin(x)[2:].zfill(32)
    # print('HERE :: ', c, con, len(con))
    return con