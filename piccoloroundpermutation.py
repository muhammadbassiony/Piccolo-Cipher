# Pass 64 bit and returns 64 bit
def round_permutation(X):

    x8 = []

    for i in range(0, 64, 8):
        x8.append(X[i:i+8])
        # print(i, i+8, X[i:i+8])

    new_x8 = []
    new_x8.append(x8[2])
    new_x8.append(x8[7])
    new_x8.append(x8[4])
    new_x8.append(x8[1])
    new_x8.append(x8[6])
    new_x8.append(x8[3])
    new_x8.append(x8[0])
    new_x8.append(x8[5])

    new_X = []
    new_X.append(new_x8[0]+new_x8[1])
    new_X.append(new_x8[2] + new_x8[3])
    new_X.append(new_x8[4] + new_x8[5])
    new_X.append(new_x8[6] + new_x8[7])

    return new_X