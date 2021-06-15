
def create_blocks(string):
    str_binary = ' '.join(format(ord(x), 'b') for x in string)
    fullblock = ''

    for x in str_binary:
        if x != ' ':
            fullblock += x

    fullblock = str(fullblock)

    blocks = []

    #create blocks and add padding
    for x in fullblock:
        if(fullblock == ' '):
            break
        if(len(fullblock) < 64):
            b = fullblock
            l = len(fullblock)
            n = '0' * (64 - l)
            new_block = b + n
            fullblock = ' '
        else:
            new_block = fullblock[0:64]
            fullblock = fullblock[64:]

        blocks.append(new_block)
        # print('BLOCK CUT ::  ', fullblock)


    return blocks


def create_blocks_decipher(string):
    #much simpler as its already padded from the encryption
    blocks = []
    for k in range(0, len(string), 64):
        b = string[k:k+64]
        # print(k, k+64, len(b))
        blocks.append(b)

    return blocks