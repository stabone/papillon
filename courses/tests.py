from django.test import TestCase
from users.models import CustomUser
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

    def setUp(self):
        self.category = Categories.objects.create(course=random_string())
        self.author = CustomUser.objects.create_user(email='test@epasts.lv', password='password')
        self.title = 'Test title'
        self.description = 'Description for test'
        self.tags = 'test'

        tut = Tuts.objects.create(
                                category=self.category,
                                author=self.author,
                                title=self.title,
                                description=self.description,
                                tags=self.tags)
        tut.save()

    def test_tut_creation(self):
        tut = Tuts.objects.get(id=1)

        self.assertEqual(self.title, tut.title)

    def test_post_flag(self):
        tut = Tuts.objects.get(id=1)

        self.assertFalse(tut.post, msg='Post for tut is True')
