import piccolokeyscheduling, piccoloffunction, piccoloroundpermutation
from utils import split_bits


def encrypt(X, key, wk,rk, bit):
    print('X RECEIVED PARAM ENCRYPT ::  ', hex(X), 'WK :: ', len(wk),  'RK :: ', len(rk))

    if bit == 80:
        r = 25
    elif bit == 128:
        r = 31

    x = split_bits(X, 16)
    print('SPLIT BLOCK :: ', [hex(m) for m in x])

    x[0] = x[0] ^ wk[0]
    x[2] = x[2] ^ wk[1]
    print('FIRST  :: ', [hex(m) for m in x])

    # f = piccoloffunction.ffunction(x[0])
    # print(f, hex(f),len(bin(f)[2:]))
    # f = piccoloffunction.ffunction(f)
    # print(f, hex(f), len(bin(f)[2:]))
    # d = piccoloroundpermutation.round_permutation(X)
    # print(d, [hex(x) for x in d])

    # F-fn takes a 16-bit block and returns a 16-bit block
    # RP fn takes 1 64-bit block and returns it as 4 16-bit blocks

    # r = 4
    for i in range(0, r-2, 1):
        print('\nOIII NEW ROUND HERE  :: ', i)

        f1 = piccoloffunction.ffunction(x[0])
        xr1 = x[1] ^ f1 ^ rk[2*i]
        x[1] = xr1
        print('1ST R  :: ', i, hex(x[0]), hex(f1), type(f1), hex(rk[2*i]), hex(x[1]), hex(xr1))
        # xr1 = xor_bin(x[1], f1)
        # xr2 = xor_bin(xr1, rk[2*i])
        # x[1] = xr2
        #
        f2 = piccoloffunction.ffunction(x[2])
        xr2 = x[3] ^ f2 ^ rk[2 * i + 1]
        x[3] = xr2
        print('2ND R  :: ', i, hex(x[3]))
        # xr3 = xor_bin(x[3], f2)
        # xr4 = xor_bin(xr3, rk[2*i + 1])
        # x[3] = xr4
        print('BEFORE RP :: ', [hex(m) for m in x])

        # xp = ''.join([ "{0:04x}".format(j) for j in x])
        xp = ''
        for j in range(0, len(x)):
            xp = ''.join([xp, "{0:04x}".format(x[j])])
        xp = int(xp, 16)
        print('XPXPXPXP ::: ', i, [hex(j) for j in x], hex(xp), len(bin(xp)[2:]))

        x = piccoloroundpermutation.round_permutation(xp)
        # loop done
        print('LOOP END :: ', i, [hex(m) for m in x])

    print('\nLOOP FINI :: ', [hex(m) for m in x])

    f1 = piccoloffunction.ffunction(x[0])
    xr1 = x[1] ^ f1 ^ rk[2 * r - 2]
    x[1] = xr1

    f2 = piccoloffunction.ffunction(x[2])
    xr2 = x[3] ^ f2 ^ rk[2 * r - 1]
    x[3] = xr2

    # print('THIRD PART DONE :: ', [hex(m) for m in x])

    x[0] = x[0] ^ wk[2]
    x[2] = x[2] ^ wk[3]

    # print('FOURTH PART DONE :: ', [hex(m) for m in x])


    e = ''
    for i in range(0, len(x)):
        e = ''.join([e, "{0:04x}".format(x[i])])

    Y = int(e, 16)
    # print('Y done :: ', hex(Y), Y)


    return Y

