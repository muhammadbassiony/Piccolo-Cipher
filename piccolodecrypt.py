import piccolokeyscheduling, piccoloencrypt, piccoloffunction, piccoloroundpermutation

def decrypt(X, key,wk,rk, bit):
    #wk = piccolokeyscheduling.generate_white_keys(bit, key)
    #rk = piccolokeyscheduling.generate_round_keys(bit, key)

    new_rk = rk
    new_wk = []
    new_wk.append(wk[2])
    new_wk.append(wk[3])
    new_wk.append(wk[0])
    new_wk.append(wk[1])

    r = 0
    if bit == 80:
        r = 25
    else:
        r = 31

    for i in range(r - 1):
        rk[2 * i] = rk[(2 * r) - (2 * i) - 2] if (i % 2 == 0) else rk[(2 * r) - (2 * i) - 1]
        rk[(2 * i) + 1] = rk[(2 * r) - (2 * i) - 2] if (i % 2 == 0) else rk[(2 * r) - (2 * i) - 1]


    x16 = convert64ToFour16s(X)
    x16[0] = x16[0] ^ wk[0]
    x16[2] = x16[2] ^ wk[1]
    r = 0
    if bit == 80:
        r = 25
    else:
        r = 31

    for i in range(r - 2):
        z=piccoloffunction.ffunction(x16[0])
        x16[1] = x16[1] ^ z ^ rk[2 * i]
        x16[3] = x16[3] ^ piccoloffunction.ffunction(x16[2]) ^ rk[(2 * i) + 1]
        x16 = convert64ToFour16s(piccoloroundpermutation.round_permutation(convertFour16sTo64(x16)))

    x16[1] = x16[1] ^ piccoloffunction.ffunction(x16[0]) ^ rk[(2 * r) - 2]
    x16[3] = x16[3] ^ piccoloffunction.ffunction(x16[2]) ^ rk[(2 * r) - 1]
    x16[0] = x16[0] ^ wk[2]
    x16[2] = x16[2] ^ wk[3]
    out=convertFour16sTo64(x16)
    return out
def convert64ToFour16s(X):
    
    x16 = []
    for i in range(4):
        x16.append((X >> (16 * (3 - i))) & 0xffff)
    return x16
    

# Pass 16 bit array of length 4 and returns 64 bit data
def convertFour16sTo64(x16):
    X = 0
    for i in range(4):
        X = X | (x16[i] << (16 * (3 - i)))
    return X