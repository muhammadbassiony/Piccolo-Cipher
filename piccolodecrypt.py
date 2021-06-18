import piccolokeyscheduling, piccoloencrypt, piccoloffunction, piccoloroundpermutation
import numpy as np

def decrypt(Y, key,wk,rk, bit):

    r = 25
    rk_new = np.zeros((2 * r), dtype=int)
    if bit == 128:
        r = 31
        rk_new = np.zeros((2 * r + 1), dtype=int)

    temp = wk.copy()
    wk[0] = temp[2]
    wk[1] = temp[3]
    wk[2] = temp[0]
    wk[3] = temp[1]


    for i in range(r):
        if i%2 == 0:
            rk_new[2*i] = rk[(2*r) - (2*i) - 2]
            rk_new[(2*i) + 1] = rk[(2*r) - (2*i) - 1]

        elif i%2 == 1:
            rk_new[2 * i] = rk[(2 * r) - (2 * i) - 1]
            rk_new[(2 * i) + 1] = rk[(2 * r) - (2 * i) - 2]


    # pass to the encryption fn again
    x = piccoloencrypt.encrypt(Y, key, wk, rk_new, bit)


    return x

