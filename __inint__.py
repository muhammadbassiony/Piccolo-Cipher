from piccolo import Piccolo

p = Piccolo(bit=128)

cipher = p.encrypt("helloworld")
print('CIPHER DONE :: ', cipher, len(cipher))

plain = p.decrypt(cipher)
print(plain)