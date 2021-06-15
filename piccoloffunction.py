from pyfinite import ffield

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
def ffunction(x):
    #print(x)
    x4 = []
    for i in range(4):
        n=(x >> (4 * (3 - i))) & 0xf
        x4.append(hex(n))
    for i in range(len(x4)):
        z=int(x4[i], 16)
        x4[i]=hex(sbox[z])
        
    F = ffield.FField(16)
    x4d = []
    for i in range(4):
        for k in range(4):
            sum = 0
            sum += F.Multiply(M[i][k], int(x4[k],16))
        x4d.append(sum)

    new_x = 0
    for i in range(4):
        new_x = new_x | (x4d[i] << (4 * (3 - i)))
        #print(bin(new_x[i]))
    return new_x