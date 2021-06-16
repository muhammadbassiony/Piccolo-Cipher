from piccolo import Piccolo

bit = 80
key80 = 0x1169207e11f0ffee1476
key128 = 0x433c6ab617af29a3c8163fad92c3d834

p = Piccolo(key=key80, bit=bit)

cipher = p.encrypt("hellomaxineandmark")
# print(cipher)
# print('Encrypting "abcdef0123456789abcdef0123456789" and \nthe cipher text is : \n', cipher)

plain = p.decrypt(cipher)
print(plain)