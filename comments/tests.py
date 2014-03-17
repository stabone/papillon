from django.test import TestCase
from comments.models import MaterialComments, PollComments

""" nead models for test data creating
class MaterialCommentsTest(TestCase):
    def setUp(self):
		obj = MaterialComments.objects.create()
		obj.save()

    def test_material_creation(self):
        obj = MaterialComments.objects.get(id=self.pk)
        self.assertEqual(obj.course, self.random_str)


class PollCommentsTest(TestCase):
    def setUp(self):
        obj = PollComments.objects.create()
        obj.save()
        self.pk = obj.id

    def test_comment_creation(self):
        obj = PollComments.objects.get(id=self.pk)
        self.assertEqual(obj.id, self.pk)
"""

