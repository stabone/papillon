from django.test import TestCase
from comments.models import MaterialComments, PollComments
from polls.models import Polls
from users.models import CustomUser

from helper.utils import random_string


"""
class MaterialCommentsTest(TestCase):
    def setUp(self):
        user_obj = CustomUser.objects.create_user(user_name='Ivars',password='naglis',email='epasts@epasts.lv')
        material = how to test file upload???
        obj = MaterialComments.objects.create(user=user_obj,material=)
        obj.save()

    def test_material_creation(self):
        obj = MaterialComments.objects.get(id=self.pk)
        self.assertEqual(obj.course, self.random_str)
"""


class PollCommentsTest(TestCase):
    def setUp(self):
        user_obj = CustomUser.objects.create(user_name='Ivars',password='Naglis',email='epasts@epasts.lv')
        poll_obj = Polls.objects.create(user=user_obj,poll=random_string())
        obj = PollComments.objects.create(user=user_obj,poll=poll_obj,comment=random_string(max=600))
        obj.save()
        self.pk = obj.id

    def test_comment_creation(self):
        obj = PollComments.objects.get(id=self.pk)
        self.assertEqual(obj.id, self.pk)


