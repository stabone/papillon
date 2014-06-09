from django.test import TestCase
from users.models import UsersExtra

from django.contrib.auth.models import User


class UsersTest(TestCase):
    def setUp(self):
        user_obj = User.objects.create_user(username='Ivars',password='naglis',email='epasts@epasts.lv')
        obj = UsersExtra.objects.create(user=user_obj,email='stabone@inbox.lv',password='12345678')
        obj.save()


    def test_user_creating(self):
        obj = UsersExtra.objects.get(id=1)
        self.assertEqual(obj.email, 'stabone@inbox.lv')
