import piccolokeyscheduling, piccoloffunction, piccoloroundpermutation


def xor_bin(x, y):
    # print('here', x, y)
    a = int(x, 2)
    b = int(y, 2)
    # print(a, b)
    z = bin(a ^ b)[2:].zfill(16)
    # print(z)
    return z


def encrypt(X, key, wk,rk, bit):
    #wk = piccolokeyscheduling.generate_white_keys(bit, key)
    #rk = piccolokeyscheduling.generate_round_keys(bit, key)
    # print('X RECEIVED PARAM ENCRYPT ::  ', X, '\nWK :: ', len(wk), wk, '\nRK :: ', len(rk), rk)

    if bit == 80:
        r = 25
    elif bit == 128:
        r = 31

    x = []
    x_hex = []
    for i in range(0, len(X), 16):
        a = X[i:i+16]
        x.append(a)
        x_hex.append(hex(int(a, 2)))

    # print('X DIVIDED', x, x_hex)

    wk_b = []
    for w in wk:
        wk_b.append(bin(int(w, 16))[2:].zfill(16))
    # print(wk, wk_b)


    x[0] = xor_bin(x[0], wk_b[0])
    x[2] = xor_bin(x[2], wk_b[1])
    # print('TEST :: ', x)

    # f = piccoloffunction.ffunction(x[0])

    for i in range(0, r-2):

        f1 = piccoloffunction.ffunction(x[0])
        xr1 = xor_bin(x[1], f1)
        xr2 = xor_bin(xr1, rk[2*i])
        x[1] = xr2

        f2 = piccoloffunction.ffunction(x[2])
        xr3 = xor_bin(x[3], f2)
        xr4 = xor_bin(xr3, rk[2*i + 1])
        x[3] = xr4

        xp = ''.join([j for j in x])
        # print(x, xp, len(xp))

        x = piccoloroundpermutation.round_permutation(xp)

    #loop done
    # print('LOOP OVER :: ', x)

    f1 = piccoloffunction.ffunction(x[0])
    xr1 = xor_bin(x[1], f1)
    xr2 = xor_bin(xr1, rk[2*r - 2])
    x[1] = xr2

    f2 = piccoloffunction.ffunction(x[2])
    xr3 = xor_bin(x[3], f2)
    xr4 = xor_bin(xr3, rk[2*r - 1])
    x[3] = xr4

    x[0] = xor_bin(x[0], wk_b[2])
    x[2] = xor_bin(x[2], wk_b[3])

    # print('FINAL :: ', x)

    Y = ''.join([m for m in x])
    # print(Y, len(Y))


    return Y

