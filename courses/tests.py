from django.test import TestCase
from django.contrib.auth.models import User
from courses.models import Categories, Tuts

from helper.utils import random_string


class CategoriesTest(TestCase):

	def setUp(self):
		self.random_str = random_string()
		obj = Categories.objects.create(course=self.random_str)
		obj.save()
		self.pk = obj.id

	def test_category_creation(self):
		obj = Categories.objects.get(id=self.pk)
		self.assertEqual(obj.course, self.random_str)


class TutsTest(TestCase):
	def setup(self):
		pass

	def test_tut_creation(self):
		pass
