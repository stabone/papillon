import string
import random


# Create your tests here.
def random_len(min,max): # 255 set for varchar fields
    return random.choice(range(min, max))


def random_string(min=3,max=255):
    length = random_len(min,max)
    return ''.join(random.choice(string.ascii_letters) for i in range(length))
