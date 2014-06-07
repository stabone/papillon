import string
import random


# Create your tests here.
def random_len(min=3, max=255): # 255 set for varchar fields
	return random.choice(range(min, max))


def random_string():
	length = random_len()
	return ''.join(random.choice(string.ascii_letters) for i in range(length))
