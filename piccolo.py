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
        cipher = []

        #create 64-bit blocks and add padding
        blocks = utils.create_blocks(string)
        # blocks = [string]


        for b in blocks:
            x = piccoloencrypt.encrypt(b, self.key, self.wk, self.rk, self.bit)
            cipher.append(x)



        ciphertext = ''
        for c in cipher:
            cb = bin((c))[2:].zfill(64)
            ciphertext = ''.join([ciphertext, cb])

        cipher_d = int(ciphertext, 2)

        return cipher_d


    def decrypt(self, fullcipher):
        decipher = []
        string = ""

        # create 64-bit blocks and add padding
        blocks = split_bits(fullcipher, 64)


        for b in blocks:
            d = piccolodecrypt.decrypt(b, self.key,self.wk,self.rk, self.bit)
            decipher.append(d)
            # break

        # TODO :: need to concat the deciphered blocks agaion here

        return string


# **************************
