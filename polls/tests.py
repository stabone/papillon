from django.test import TestCase
from polls.models import Polls, Questions, Choises

from helper.utils import random_string


class PollTest(TestCase):

	def setUp(self):
		self.random_str = random_string()
		obj = Polls.objects.create(poll=self.random_str)
		obj.save()
		self.pk = obj.id

	def test_poll_creating(self):
		obj = Polls.objects.get(id=self.pk)
		self.assertEqual(obj.poll, self.random_str)


class QuestionTest(TestCase):
	def setUp(self):
		self.question = "5 x 5 is?"
		poll = Polls.objects.create(poll="test poll")
		question = Questions.objects.create(poll=poll, question=self.question)
		question.save()
		self.question_id = question.id

	def test_question_creating(self):
		obj = Questions.objects.get(id=self.question_id)
		self.assertEqual(obj.question, self.question)


class Choises(TestCase):
    pass


