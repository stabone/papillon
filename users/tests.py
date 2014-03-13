from django.test import TestCase
from users.models import Users


class UsersTest(TestCase):
    def setUp(self):
        obj = Users.objects.create(username='ivars',lastname='naglis',email='stabone@inbox.lv')
        obj.save()


    def test_user_creating(self):
        obj = Users.objects.get(email='stabone@inbox.lv')
        self.assertEqual(obj.username, 'ivars')
