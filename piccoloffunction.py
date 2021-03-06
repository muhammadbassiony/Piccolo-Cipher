from pyfinite import ffield
import galois
import numpy as np
from utils import split_bits, concat_split_num



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

    x = split_bits(X, 4)

    while(len(x) <  4):
        x.insert(0, 0)


    #first s-box
    temp = x
    for d in range(len(x)):
        x[d] = sbox[temp[d]]

    # we are working in Galois Field of 2^4 as described by the paper
    # create a Galois Field object
    GF256 = galois.GF(2 ** 4)

    # check that the irreducable poly is the same as described in the paper
    # print(GF256.properties)
    # print(GF256.irreducible_poly)

    # converting our diffusion matrix to be in the field
    M_GF = GF256(M)

    # convert X into the galois field
    x_GF = GF256(x)

    # perform the matrix multiplication
    res = np.matmul(M_GF, x_GF.T)

    # convert back to a normal array
    res_int = np.array(res)

    # second s-box
    temp = res_int
    for d in range(len(x)):
        x[d] = sbox[temp[d]]


    #join the output into 1 16-bit block

    new_x = 0
    for i in range(4):
        new_x = new_x | (x[i] << (4 * (3 - i)))


    return new_x

