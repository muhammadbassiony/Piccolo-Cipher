from piccolo import Piccolo


p = Piccolo(bit=128)
cipher = p.encrypt("helloworld")
#plain=p.decrypt(cipher)
print(cipher)
# print(plain)