from pyfinite import ffield
import galois
import numpy as np


# S-Box Layer
sbox = {
    0x0: 0xe,
    0x1: 0x4,
    0x2: 0xb,
    0x3: 0x2,
    0x4: 0x3,
    0x5: 0x8,
    0x6: 0x0,
    0x7: 0x9,
    0x8: 0x1,
    0x9: 0xa,
    0xa: 0x7,
    0xb: 0xf,
    0xc: 0x6,
    0xd: 0xc,
    0xe: 0x5,
    0xf: 0xd
}

# Diffusion Matrix
M = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]

# Pass 16 bit data and returns 16 bit data
def ffunction(X):
    # print('FFUNCTION BRO :: PARAM :: ', X, len(X), type(X))

    x = []
    x_hex = []
    x_dec = []

    for i in range(0, len(X), 4):
        x.append(X[i:i + 4])
        x_hex.append(hex(int(X[i:i + 4], 2)))
        x_dec.append(int(X[i:i + 4], 2))

    # print(x, len(x[0]), x_hex)

    #first s-box
    x_s1 = []
    x_s1_dec = []
    for z in x_hex:
        a = sbox[0+int(z, 16)]
        x_s1.append(hex(a))
        x_s1_dec.append(a)

    # print(x_s1, x_s1_dec)


    #we are working in Galois Field of 2^4 as described by the paper
    # a = 7
    # F = ffield.FField(4)
    # print(F.ShowPolynomial(a))

    #create a Galois Field object
    GF256 = galois.GF(2 ** 4)
    # check that the irreducable poly is the same as described in the paper
    # print(GF256.properties)
    # print(GF256.irreducible_poly)

    #converting our diffusion matrix to be in the field
    M_GF = GF256(M)
    #print('MATRIX IN GF(4) ::  ', M)

    #convert X into the galois field
    x_s1_GF = GF256(x_s1_dec)
    #print('X_s1 in GF ::  ', x_s1_GF)

    #perform the matrix multiplication
    res = np.matmul(M_GF, x_s1_GF.T)
    #print('RESULT OF MATRIX MULT IN GF(4) :: ', res)

    #convert back to a normal array
    res_int = np.array(res)
    #print(res_int)

    x_mult_hex = []
    x_mult_dec = []
    for c in res_int:
        a = int(c)
        a = hex(sbox[0+int(a)])
        x_mult_dec.append(int(a, 16))
        x_mult_hex.append(a)

    print(x_mult_hex, x_mult_dec)


    return  " "