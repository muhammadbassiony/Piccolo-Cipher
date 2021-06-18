import piccolokeyscheduling, piccoloffunction, piccoloroundpermutation
from utils import split_bits


def encrypt(X, key, wk,rk, bit):

    if bit == 80:
        r = 25
    elif bit == 128:
        r = 31

    x = split_bits(X, 16)

    x[0] = x[0] ^ wk[0]
    x[2] = x[2] ^ wk[1]

    # F-fn takes a 16-bit block and returns a 16-bit block
    # RP fn takes 1 64-bit block and returns it as 4 16-bit blocks

    for i in range(0, r-1, 1):
        f1 = piccoloffunction.ffunction(x[0])
        xr1 = x[1] ^ f1 ^ rk[2*i]
        x[1] = xr1

        f2 = piccoloffunction.ffunction(x[2])
        xr2 = x[3] ^ f2 ^ rk[2 * i + 1]
        x[3] = xr2

        xp = ''
        for j in range(0, len(x)):
            xp = ''.join([xp, "{0:04x}".format(x[j])])
        xp = int(xp, 16)

        x = piccoloroundpermutation.round_permutation(xp)




    f1 = piccoloffunction.ffunction(x[0])
    xr1 = x[1] ^ f1 ^ rk[2 * r - 2]
    x[1] = xr1

    f2 = piccoloffunction.ffunction(x[2])
    xr2 = x[3] ^ f2 ^ rk[2 * r - 1]
    x[3] = xr2

    x[0] = x[0] ^ wk[2]
    x[2] = x[2] ^ wk[3]


    # joining x
    e = ''
    for i in range(0, len(x)):
        e = ''.join([e, "{0:04x}".format(x[i])])

    Y = int(e, 16)

    return Y

