from django.test import TestCase
from polls.models import Polls
import string
import random

# Create your tests here.
# Create your tests here.
def random_len(min=3, max=255): # 255 set for varchar fields
	return random.choice(range(min, max))


def random_string(length=6):
	return ''.join(random.choice(string.ascii_letters) for i in range(length))


class CategoriesTest(TestCase):

	def setUp(self):
		length=random_len()
		self.random_str=random_string(length)
		obj=Polls.objects.create(question=self.random_str)
		obj.save()
		self.pk=obj.id

	def test_poll_creating(self):
		obj=Polls.objects.get(id=self.pk)
		self.assertEqual(obj.question, self.random_str)

