import numpy as np
from utils import split_bits

class InvalidValue(Exception):
    def __init__(self, expression, message):
        self.expression = message
        self.message = message



def generate_white_keys(bit, key):
    # print('GEN WHITE KEYS :: PAR4AMS ::: ', bit, key)
    ikey = int(key)
    k = []
    wk = []

    # print('ENTERING SPLITTER :: ', bit, hex(key))
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
    # print('GEN ROUND KEYS :: PAR4AMS ::: ', bit, hex(key))
    ikey = int(key)
    skey = str(key)
    k = []
    rk = []
    sbit = int(bit / 16)

    k = split_bits(key, 16)
    # print('KEY SPLIT IN RK ::: ', [hex(x) for x in k])

    if bit == 80:
        r = 25
    elif bit == 128:
        r = 31


    # rk = np.zeros((2*r + 2), dtype=int)
    # cons = np.zeros((2*r + 2), dtype=int)
    # print(rk.shape, cons.shape, type(cons), (2*r + 1), 2*r-1)
    # print('ZERO CHECK :: ', [hex(x) for x in cons])


    if bit == 80:

        rk = np.zeros((2 * r ), dtype=int)
        cons = np.zeros((2 * r ), dtype=int)
        # print('RK80 SHAPES :: ',rk.shape, cons.shape, type(cons), (2 * r + 1), 2 * r - 1)

        for i in range(r-1):
            #generate constant
            left, right = get_contsant_values(i, bit)
            cons[2*i] = left
            cons[(2*i)+1] = right
            # print('CON80 RK :: ', i, hex(l), hex(r), hex(cons[2*i]), hex(cons[(2*i)+1]))

            if i % 5 == 2 or i % 5 == 0:
                z = cons[2*i] ^ k[2]
                rk[2*i] = z

                z = cons[(2*i)+1] ^ k[3]
                rk[2*i + 1] = z

            elif i % 5 == 1 or i % 5 == 4:
                z = cons[2 * i] ^ k[0]
                rk[2 * i] = z

                z = cons[(2*i)+1] ^ k[1]
                rk[2 * i + 1] = z

            elif i % 5 == 3:
                z = cons[2 * i] ^ k[4]
                rk[2 * i] = z

                z = cons[(2*i)+1] ^ k[4]
                rk[2 * i + 1] = z

        # print('DONE 80 RK GEN :: ')

    elif bit == 128:

        rk = np.zeros((2 * r + 1), dtype=int)
        cons = np.zeros(2 * (2 * r + 1), dtype=int)
        # print('RK128 SHAPES :: ', rk.shape, cons.shape, type(cons), (2 * r + 1), 2 * r - 1)

        for i in range((2*r) - 1):
            # generate constant
            left, right = get_contsant_values(i, bit)
            cons[2 * i] = left
            cons[(2*i)+1] = right
            # print('\nCON128 RK :: ', i, hex(left), hex(right), hex(cons[2*i]), hex(cons[(2*i)+1]))


            # print('KEY BEFORE :: ', [hex(x) for x in k])
            if (i + 2) % 8 == 0:
                # print('SWITCHEROO', [hex(x) for x in k])
                tmp = k
                k[0] = tmp[2]
                k[2] = tmp[6]
                k[3] = tmp[7]
                k[4] = tmp[0]
                k[5] = tmp[3]
                k[6] = tmp[4]
                k[7] = tmp[5]
                # print('KEY AFTER :: ', [hex(x) for x in k])

            indx = (i + 1) % 8
            z = k[indx] ^ cons[i]
            rk[i] = z

    else:
        raise InvalidValue('bit=' + str(bit), 'The value of bit can be 80 or 128')

    print('ROUND KEYS GENNED :: ', [hex(x) for x in rk])
    return rk



def get_contsant_values(i, bit):

    cnn = 0x0f1e2d3c if bit==80 else 0x6547a98b
    ci_1 = (i + 1)
    cc = (ci_1 << 27) | (0 << 22) | (ci_1 << 17) | (0 << 15) | (ci_1 << 10) | (0 << 5) | (ci_1)

    cons = cc ^ cnn
    left = cons >> 16
    right = cons & 0xffff

    return (left, right)

