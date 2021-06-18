

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



def concat_split_num(a):

    s = ''
    for i in a:
        s += hex(i)[2:]
        # print('UTILS ::: ', s)

    s = int(s, 16)

    return s


def create_blocks(string):
    str_binary = ' '.join(format(ord(x), 'b') for x in string)
    # print('STR BINARRY :: ', int(string))

    fullblock = str_binary.replace(" ", "")
    # fullblock = "011010000110010101101100011011000110111101101101011000010111100001101001011011100110010101100001011011100110010001101101011000010111001001101011"
    blocks = []
    # print('NEW FULLBLOCK', len(fullblock))

    # create blocks
    while len(fullblock) >= 64:
        l = len(fullblock)
        sub = fullblock[l-64:l]
        # print('SUB :: ', sub, len(sub))
        fullblock = fullblock[:l-64]
        blocks.append(int(sub, 2))

    # print('LAST BLOCK :: ', fullblock, len(fullblock))

    # add padding to the last block
    if len(fullblock) != 0:
        diff = 64 - len(fullblock)
        s = fullblock + ('0'*diff)
        blocks.append(int(s, 2))

    # for b in blocks:
    #     h = bin(b)[2:]
    #     print('BLOCK :: ', hex(b), len(h))

    return blocks


def create_blocks_decipher(fullcipher):
    #much simpler as its already padded from the encryption
    # print('CREATE DECIPHERING BLOCKS :: ', fullcipher, hex(fullcipher)[2:], len(hex(fullcipher)[2:]) / 16)
    # num_blocks = int(len(hex(fullcipher)[2:]) / 16)
    # print('NUM BLOCKS :: ', num_blocks)

    blocks = split_bits(fullcipher, 64)
    print('RESULTING BLOCKS :: ', [hex(x) for x in blocks])

    # for k in range(0, len(string), 64):
    #     b = string[k:k+64]
    #     # print(k, k+64, len(b))
    #     blocks.append(b)
    #
    # return blocks


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