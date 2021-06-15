import piccolokeygen, piccoloencrypt, piccolodecrypt, piccolokeyscheduling, utils
import binascii

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

        for b in blocks:

            x = piccoloencrypt.encrypt(b, self.key, self.wk, self.rk, self.bit)
            cipher.append(x)


        estring = ''.join([c for c in cipher])

        return estring


    def decrypt(self, estring):
        hexlist = []
        decipher = []
        string = ""

        print('DECIPHER  1 :: ', estring, type(estring))
        # create 64-bit blocks and add padding
        blocks = utils.create_blocks_decipher(estring)
        print('BLOCKS :: ', blocks)

        for b in blocks:
            print('ENTERING DECRYPT :: ', len(b), b)
            d = piccolodecrypt.decrypt(b, self.key,self.wk,self.rk, self.bit)
            break

        # for i in range(0,len(estring),16):
        #     hexlist.append(estring[i:i+16])
        #
        # for i in range(len(hexlist)):
        #     decipher.append(piccolodecrypt.decrypt(int(hexlist[i], 16), self.key,self.wk,self.rk, self.bit))
        #
        # print(decipher)
        #
        # for i in range(len(decipher)):
        #     string+=(format(decipher[i], 'x'))

        return string


# **************************
