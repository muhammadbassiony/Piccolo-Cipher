from pyfinite import ffield
import galois
import numpy as np
from utils import split_bits, concat_split_num



def split_bits_ffn(value, n):

    mask, parts = (1 << n) - 1, []
    # print('MASK :: ', hex(mask), bin(mask))
    parts = []
    while value:
        parts.append(value & mask)
        # print('APPENDED VAL :: ', hex(value & mask))
        value >>= n
        # print('NEW VAL/SHIFTED :: ', hex(value))

    parts.reverse()
    # print('PARTS AFTER REVERSAL :: ', [hex(x) for x in parts])
    return parts



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
    print('*'*20)
    print('FFUNCTION BRO :: PARAM :: ', hex(X))

    x = split_bits(X, 4)
    print('SPLIT BLOCK IN F-FN:: ', len(x), [m for m in x], [hex(m) for m in x])

    while(len(x) <  4):
        print('HERE PREPENDING X :: ', len(x), [m for m in x], [hex(m) for m in x])
        x.insert(0, 0)

    print('F-FN PREPENDING BEFORE 1ST SBLOCK:: ', len(x), [m for m in x], [hex(m) for m in x])

    #first s-box
    temp = x
    for d in range(len(x)):
        x[d] = sbox[temp[d]]

    # print('1ST S-BOX DONE :: ', [hex(m) for m in x])

    #we are working in Galois Field of 2^4 as described by the paper
    #create a Galois Field object
    GF256 = galois.GF(2 ** 4)

    # check that the irreducable poly is the same as described in the paper
    # print(GF256.properties)
    # print(GF256.irreducible_poly)

    #converting our diffusion matrix to be in the field
    M_GF = GF256(M)
    # print('MATRIX IN GF(4) ::  ', M)

    #convert X into the galois field
    x_GF = GF256(x)
    # print('X in GF ::  ', x_GF)

    #perform the matrix multiplication
    res = np.matmul(M_GF, x_GF.T)
    # print('RESULT OF MATRIX MULT IN GF(4) :: ', res)

    #convert back to a normal array
    res_int = np.array(res)
    # print('RES :: ', res_int, [hex(m) for m in res_int])

    # second s-box
    temp = res_int
    for d in range(len(x)):
        x[d] = sbox[temp[d]]

    # print('2ND S-BOX DONE :: ', x, [hex(m) for m in x])

    #join the output into 1 16-bit block
    # s = concat_split_num(x)

    new_x = 0
    for i in range(4):
        new_x = new_x | (x[i] << (4 * (3 - i)))

    print('JOINED F-FN OUTPUT :: ', hex(new_x))
    print('*' * 20)
    return new_x

