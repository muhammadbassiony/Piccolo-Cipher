from piccolo import Piccolo

bit = 80
key = 0x1169207e11f0ffee1476

p = Piccolo(key=key, bit=80)

cipher = p.encrypt("hellomax")
# print(cipher)
# print('Encrypting "abcdef0123456789abcdef0123456789" and \nthe cipher text is : \n', cipher)

plain = p.decrypt(cipher)
print(plain)