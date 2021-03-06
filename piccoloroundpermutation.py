
from utils import split_bits, concat_split_num

# Pass 64 bit and returns 64 bit
def round_permutation(X):
    x = split_bits(X, 8)

    # in case the leading zeros were not counted
    while len(x) < 8:
        x.insert(0, 0)


    x8 = []
    x8.append(x[2])
    x8.append(x[7])
    x8.append(x[4])
    x8.append(x[1])
    x8.append(x[6])
    x8.append(x[3])
    x8.append(x[0])
    x8.append(x[5])


    new_X = []
    j = 2
    for i in range(0, len(x8), 2):
        m = (x8[i]<<8 & 0xffff) | (x8[i+1] & 0xffff)
        new_X.append(m)


    return new_X