
# this function takes an int value and divides it into blocks of n bits
def split_bits(value, n):
    mask, parts = (1 << n) - 1, []
    parts = []
    while value:
        parts.append(value & mask)
        value >>= n

    parts.reverse()
    return parts



def concat_split_num(a):
    s = ''
    for i in a:
        s += hex(i)[2:]

    s = int(s, 16)

    return s


# TODO :: reimplement the text-to-binary functionality
def create_blocks(string):
    str_binary = ' '.join(format(ord(x), 'b') for x in string)

    fullblock = str_binary.replace(" ", "")
    # fullblock = "011010000110010101101100011011000110111101101101011000010111100001101001011011100110010101100001011011100110010001101101011000010111001001101011"
    blocks = []

    # create blocks
    while len(fullblock) >= 64:
        l = len(fullblock)
        sub = fullblock[l-64:l]
        fullblock = fullblock[:l-64]
        blocks.append(int(sub, 2))

    # add padding to the last block
    if len(fullblock) != 0:
        diff = 64 - len(fullblock)
        s = fullblock + ('0'*diff)
        blocks.append(int(s, 2))


    return blocks

"""
def create_blocks_decipher(fullcipher):
    #much simpler as its already padded from the encryption
    blocks = split_bits(fullcipher, 64)
"""
