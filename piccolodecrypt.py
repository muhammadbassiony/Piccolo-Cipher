import piccolokeyscheduling, piccoloencrypt, piccoloffunction, piccoloroundpermutation
import numpy as np

def decrypt(Y, key,wk,rk, bit):
    print('PICCOLO DECRYPT PARAMS :: ', Y, len(Y), '\nWK :: ', len(wk), wk, '\nRK :: ', len(rk), rk,'\n\n')

    if bit == 80:
        r = 25
    elif bit == 128:
        r = 31


    print(wk)
    temp = wk.copy()
    wk[0] = temp[2]
    wk[1] = temp[3]
    wk[2] = temp[0]
    wk[3] = temp[1]
    print(wk == temp)

    rk_new = np.array(['0'*16 for _ in range(2*r + 1)])


    for i in range(r - 1):
        if(i%2 == 0):
            rk_new[2*i] = rk[(2*r) - (2*i) - 2]
            rk_new[(2*i) + 1] =  rk[(2*r) - (2*i) - 1]

        elif(i%2 == 1):
            rk_new[2 * i] = rk[(2 * r) - (2 * i) - 1]
            rk_new[(2 * i) + 1] = rk[(2 * r) - (2 * i) - 2]

    x = piccoloencrypt.encrypt(Y, key, wk, rk_new, bit)

    return x

