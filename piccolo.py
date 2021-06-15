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

        print('init done :: ', bit, key, '\n', wk, '\n', rk)


    def getKey(self):
        return self.key

    def encrypt(self, string):
        ascii = []
        cipher = []
        estring = ""

        print('ENCRYPT 1 :: ', string)

        blocks = utils.create_blocks(string)

        for b in blocks:
            print('BLOCK ENTYERING :: ', b, len(b))
            x = piccoloencrypt.encrypt(b, self.key, self.wk, self.rk, self.bit)

        # for i in range(0,len(string),16):
        #     ascii.append(string[i:i+16])

        # print('ENCRYPT 2.1 :: ', self.bit, self.key, '\n WK :: ', self.wk, '\n RK :: ', self.rk)


        # for i in range(len(ascii)):
        #     cipher.append(piccoloencrypt.encrypt(ascii[i], self.key,self.wk,self.rk, self.bit))
        # print(cipher)
        # for i in range(len(cipher)):
        #     estring+=(format(cipher[i], 'x'))

        return estring

    def decrypt(self, estring):
        hexlist = []
        decipher = []
        string = ""

        for i in range(0,len(estring),16):
            hexlist.append(estring[i:i+16])

        for i in range(len(hexlist)):
            decipher.append(piccolodecrypt.decrypt(int(hexlist[i], 16), self.key,self.wk,self.rk, self.bit))

        print(decipher)

        for i in range(len(decipher)):
            string+=(format(decipher[i], 'x'))

        return string


# **************************
