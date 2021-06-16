import piccolokeyscheduling, piccoloffunction, piccoloroundpermutation
from utils import split_bits

def xor_bin(x, y):
    # print('here', x, y)
    a = int(x, 2)
    b = int(y, 2)
    # print(a, b)
    z = bin(a ^ b)[2:].zfill(16)

    asst = ''
    for v in range(len(y)):
        if(x[v] != y[v]):
            asst += '1'
        else:
            asst += '0'

    # print(z, asst, z==asst)
    return z


def encrypt(X, key, wk,rk, bit):
    print('X RECEIVED PARAM ENCRYPT ::  ', X, 'WK :: ', len(wk),  'RK :: ', len(rk))

    if bit == 80:
        r = 25
    elif bit == 128:
        r = 31

    x = split_bits(X, 16)
    print('SPLIT BLOCK :: ', [hex(m) for m in x])

    x[0] = x[0] ^ wk[0]
    x[2] = x[2] ^ wk[1]

    print('FIRST  :: ', [hex(m) for m in x])

    # wk_b = []
    # for w in wk:
    #     wk_b.append(bin(int(w, 16))[2:].zfill(16))
    # # print(wk, wk_b)
    #
    #
    # x[0] = xor_bin(x[0], wk_b[0])
    # x[2] = xor_bin(x[2], wk_b[1])
    # print('TEST :: ', x)

    f = piccoloffunction.ffunction(x[0])
    print(f)
    r = 3
    # for i in range(0, r-2):
    #     print('OIII :: ', i)
    #     f1 = piccoloffunction.ffunction(x[0])
    #     xr1 = xor_bin(x[1], f1)
    #     xr2 = xor_bin(xr1, rk[2*i])
    #     x[1] = xr2
    #
    #     f2 = piccoloffunction.ffunction(x[2])
    #     xr3 = xor_bin(x[3], f2)
    #     xr4 = xor_bin(xr3, rk[2*i + 1])
    #     x[3] = xr4
    #
    #     xp = ''.join([j for j in x])
    #     # print(x, xp, len(xp))
    #
    #     x = piccoloroundpermutation.round_permutation(xp)

    #loop done
    # print('LOOP OVER :: ', x)
    #
    # f1 = piccoloffunction.ffunction(x[0])
    # xr5 = xor_bin(x[1], f1)
    # xr6 = xor_bin(xr5, rk[2*r - 2])
    # x[1] = xr6
    #
    # f2 = piccoloffunction.ffunction(x[2])
    # xr7 = xor_bin(x[3], f2)
    # xr8 = xor_bin(xr7, rk[2*r - 1])
    # x[3] = xr8
    #
    # x[0] = xor_bin(x[0], wk_b[2])
    # x[2] = xor_bin(x[2], wk_b[3])


    Y = ''.join([m for m in x])
    # print(Y, len(Y))


    return "YYYYYYYY"

