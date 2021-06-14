import random

def piccolokeygen(bit):
    key = ""

    if bit == 80:
        key = "".join(random.choice('0123456789abcdef') for n in range(20))
    elif bit == 128:
        key = "".join(random.choice('0123456789abcdef') for n in range(32))

    return key