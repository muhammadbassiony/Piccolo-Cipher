

def split_bits(value, n):

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


def create_blocks(string):
    str_binary = ' '.join(format(ord(x), 'b') for x in string)

    fullblock = str_binary.replace(" ", "")
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

    # print('BLOCKSS :: ', blocks)

    return blocks


def create_blocks_decipher(string):
    #much simpler as its already padded from the encryption
    blocks = []
    for k in range(0, len(string), 64):
        b = string[k:k+64]
        # print(k, k+64, len(b))
        blocks.append(b)

    return blocks


def bin_to_text(str):
    # print('BIN TO STR :: ', str, len(str))

    s = []
    for x in range(0, len(str), 8):
        # print(x, x+8, str[x:x+8])
        b = str[x:x+7]
        i = int(b[1:], 2)
        c = chr(i)
        # print(c)
        s.append(c)

    ss = ''.join(f for f in s)
    # print()
    return ss