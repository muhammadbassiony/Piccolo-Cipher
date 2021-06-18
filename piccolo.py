import piccolokeygen, piccoloencrypt, piccolodecrypt, piccolokeyscheduling, utils
from utils import split_bits

class Piccolo:
    def __init__(self, key="", wk="", rk="", bit=80):
        if bit != 128:
            if bit != 80:
                raise ValueError

        self.bit = bit
        self.key = piccolokeygen.piccolokeygen(bit) if key == "" else key
        self.wk = piccolokeyscheduling.generate_white_keys(bit, self.key) if wk == "" else wk
        self.rk = piccolokeyscheduling.generate_round_keys(bit, self.key) if rk == "" else rk



    def getKey(self):
        return self.key

    def encrypt(self, string):
        ascii = []
        cipher = []
        estring = ""

        #create 64-bit blocks and add padding
        blocks = utils.create_blocks(string)
        # blocks = [string]
        print('ALL BLOCKS :: ', [hex(r) for r in blocks])


        for b in blocks:
            print('BLOCK ENTERING :: ', len(bin(b)[2:]), hex(b), '\n')
            x = piccoloencrypt.encrypt(b, self.key, self.wk, self.rk, self.bit)
            print('BLOCK FULLY ENCRYPTED :: ', hex(x), len(bin(x)[2:]))
            cipher.append(x)
            break

        # print('CIPHER TEXT :: ', [(hex(y),len(bin(y)[2:])) for y in cipher])

        ciphertext = ''
        for c in cipher:
            cb = bin((c))[2:].zfill(64)
            ciphertext = ''.join([ciphertext, cb])
            # print('CIPHERINIOOO :: ', c, hex(c), cb, len(cb))

        cipher_d = int(ciphertext, 2)
        # print('HERE :: ', ciphertext, len(ciphertext), '\n',hex(d), len(bin(d)[2:]))

        return cipher_d


    def decrypt(self, fullcipher):
        hexlist = []
        decipher = []
        string = ""

        print('DECIPHER  1 :: ', hex(fullcipher), len(bin(fullcipher)[2:]))

        # create 64-bit blocks and add padding
        blocks = split_bits(fullcipher, 64)
        # print('RESULTING BLOCKS :: ', [hex(x) for x in blocks])

        for b in blocks:
            print('ENTERING DECRYPT :: ', hex(b), len(bin(b)[2:]))
            d = piccolodecrypt.decrypt(b, self.key,self.wk,self.rk, self.bit)
            decipher.append(d)
            # break

        print('DECIPHERED :: ', [hex(x) for x in decipher])

        # dstr = ''.join([v for v in decipher])
        # plain = utils.bin_to_text(dstr)
        # print(estring)
        # print(dstr)
        # print(plain)

        return string


# **************************
