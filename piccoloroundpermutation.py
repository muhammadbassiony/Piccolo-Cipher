
from utils import split_bits, concat_split_num

# Pass 64 bit and returns 64 bit
def round_permutation(X):

    x = split_bits(X, 8)
    # print('SPLIT BLOCK IN R-P  :: ', len(x), [hex(m) for m in x])

    x8 = []
    x8.append(x[2])
    x8.append(x[7])
    x8.append(x[4])
    x8.append(x[1])
    x8.append(x[6])
    x8.append(x[3])
    x8.append(x[0])
    x8.append(x[5])

    # print('RP ORDER PERMUTED :: ', len(x8), [hex(m) for m in x8])

    new_X = []
    for i in range(0, len(x8), 2):
        s = hex(x8[i])[2:] + hex(x8[i+1])[2:]
        new_X.append(int(s, 16))


    # print('RP OUTPUT PERMUTATED AND CONCATENATED BABY :: ', [hex(b) for b in new_X])
    return new_X