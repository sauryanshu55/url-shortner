import string
import random

def key_generator(size=6, chars=string.ascii_uppercase + string.digits):
    key= ''.join(random.choice(chars) for _ in range(size))
    return key

