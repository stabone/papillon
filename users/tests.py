from django.test import TestCase

from django.contrib.auth.models import User
from users.models import CustomUser


class UsersTest(TestCase):
    def setUp(self):
        user = CustomUser.objects.create_user(password='naglis',email='epasts@epasts.lv')
        user.save()


    def test_user_creating(self):
        pass
        # obj = UsersExtra.objects.get(id=1)
        # self.assertEqual(obj.email, 'stabone@inbox.lv')
