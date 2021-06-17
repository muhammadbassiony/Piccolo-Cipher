from piccolo import Piccolo

bit = 80
key80 = 0x1169207e11f0ffee1476
key128 = 0x433c6ab617af29a3c8163fad92c3d834
plain = "hellomaxineandmark"

p = Piccolo(key=key80, bit=bit)

cipher = p.encrypt(plain)
print('ENCRYPTED PLAIN TEXT : %s \nRESULTING CIPHER IS : %s' % (plain, hex(cipher)), '\n\n')


decrypted = p.decrypt(cipher)
print('DECRYPTED CIPHER %s \nAND RESULTING PLAIN TEXT IS : %s' % (hex(cipher), decrypted))