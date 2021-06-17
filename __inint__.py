from piccolo import Piccolo

bit = 80

key80 = 0x00112233445566778899
result80 = 0x8d2bff9935f84056

key128 = 0x433c6ab617af29a3c8163fad92c3d834

#added a zero at the end as padding till i implement a padding fn later
plain = 0x0123456789abcdef0
# print(len(bin(plain)[2:]))

p = Piccolo(key=key80, bit=bit)

cipher = p.encrypt(plain)
print('ENCRYPTED PLAIN TEXT : %s \nRESULTING CIPHER IS : %s\nEXPECTED RESULT IS : %s' %
      (hex(plain), hex(cipher), hex(result80)), '\n\n')


# decrypted = p.decrypt(cipher)
# print('DECRYPTED CIPHER %s \nAND RESULTING PLAIN TEXT IS : %s' % (hex(cipher), decrypted))