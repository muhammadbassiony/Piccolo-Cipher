# Pass 64 bit and returns 64 bit
def round_permutation(X):
    x8 = []

    for i in range(8):
        x8.append((X >> (8 * (7 - i)) & 0xff))
    
    new_x8 = []
    new_x8.append(x8[2])
    new_x8.append(x8[7])
    new_x8.append(x8[4])
    new_x8.append(x8[1])
    new_x8.append(x8[6])
    new_x8.append(x8[3])
    new_x8.append(x8[0])
    new_x8.append(x8[5])

    new_X = 0
    for i in range(8):
        new_X = new_X | (new_x8[i] << (8 * (7 - i)))
    return new_X