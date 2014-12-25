from django.test import TestCase

from categories.models import Categories


class CategoryTest(TestCase):

    def setUp(self):
        self.title = "Python"
        category = Categories.objects.create(title=self.title)
        category.save()

    def test_creating(self):
        category = Categories.objects.get(id=1)
        self.assertEqual(self.title, category.title)
