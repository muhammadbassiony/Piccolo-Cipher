import piccolokeyscheduling, piccoloencrypt, piccoloffunction, piccoloroundpermutation
import numpy as np

def decrypt(Y, key,wk,rk, bit):

    print('DECRYPT PARAMS :: ', Y, hex(key), bit)
    print('DECRYPT PARAMS :: WHITE KEYS GENNED :: ', len(wk), [hex(x) for x in wk])
    print('DECRYPT PARAMS :: ROUND KEYS :: ', len(rk), [hex(x) for x in rk])


    r = 25
    rk_new = np.zeros((2 * r), dtype=int)

    if bit == 128:
        r = 31
        rk_new = np.zeros((2 * r + 1), dtype=int)

    # print(rk_new.shape)

    # print('WHITE KEYS BEFORE SHUFFLE :: ', len(wk), [hex(x) for x in wk])
    temp = wk.copy()
    wk[0] = temp[2]
    wk[1] = temp[3]
    wk[2] = temp[0]
    wk[3] = temp[1]
    print('WHITE KEYS AFTER SHUFFLE :: ', len(wk), [hex(x) for x in wk])

    # rk_new = np.array(['0'*16 for _ in range(2*r + 1)])


    for i in range(r - 1):
        if(i%2 == 0):
            rk_new[2*i] = rk[(2*r) - (2*i) - 2]
            rk_new[(2*i) + 1] =  rk[(2*r) - (2*i) - 1]

        elif(i%2 == 1):
            rk_new[2 * i] = rk[(2 * r) - (2 * i) - 1]
            rk_new[(2 * i) + 1] = rk[(2 * r) - (2 * i) - 2]

    # print(rk == list(rk_new).reverse())
    x = piccoloencrypt.encrypt(Y, key, wk, rk_new, bit)
    # print(Y)
    # print(x)

    return x

