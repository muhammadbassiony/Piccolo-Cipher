
from utils import split_bits, concat_split_num

# Pass 64 bit and returns 64 bit
def round_permutation(X):
    print('*' * 20)
    print('RP PARAMS :: ', hex(X))

    x = split_bits(X, 8)
    print('SPLIT BLOCK IN R-P  :: ', len(x), [hex(m) for m in x])

    x8 = []
    x8.append(x[2])
    x8.append(x[7])
    x8.append(x[4])
    x8.append(x[1])
    x8.append(x[6])
    x8.append(x[3])
    x8.append(x[0])
    x8.append(x[5])

    print('RP ORDER PERMUTED :: ', len(x8), [hex(m) for m in x8])
    # "{0:04x}".format(x[i])

    new_X = []
    j = 2
    for i in range(0, len(x8), 2):
        m = (x8[i]<<8 & 0xffff) | (x8[i+1] & 0xffff)
        new_X.append(m)


    print('RP OUTPUT PERMUTATED AND CONCATENATED BABY :: ', [hex(b) for b in new_X])
    print('*' * 20)
    return new_X