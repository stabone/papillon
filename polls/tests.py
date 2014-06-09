from django.test import TestCase
from polls.models import Polls, Questions, Choises
from django.contrib.auth.models import User

from helper.utils import random_string


class PollTest(TestCase):

    def setUp(self):
        self.random_str = random_string()
        user_obj = User.objects.create_user(username='Ivars',password='naglis',email='epasts@epasts.lv')
        obj = Polls.objects.create(user=user_obj,poll=self.random_str)
        obj.save()
        self.pk = obj.id

    def test_poll_creating(self):
        obj = Polls.objects.get(id=self.pk)
        self.assertEqual(obj.poll, self.random_str)


class QuestionTest(TestCase):
    def setUp(self):
        self.question = "5 x 5 is?"
        user_obj = User.objects.create_user(username='Ivars',password='naglis',email='epasts@epasts.lv')
        poll = Polls.objects.create(user=user_obj,poll="test poll")
        question = Questions.objects.create(poll=poll, question=self.question)
        question.save()
        self.question_id = question.id

    def test_question_creating(self):
        obj = Questions.objects.get(id=self.question_id)
        self.assertEqual(obj.question, self.question)


class ChoisesTest(TestCase):
    def setUp(self):
        self.question = random_string()
        user_obj = User.objects.create_user(username='ivars',password='naglis',email='epasts@epasts.lv')
        poll_obj = Polls.objects.create(user=user_obj,poll='muffin')
        question_obj = Questions.objects.create(poll=poll_obj,question=self.question)
        Choises.objects.create(question=question_obj,option='Yes',correct=True)
        Choises.objects.create(question=question_obj,option='No')

    def test_choise_question(self):
        record = Choises.objects.get(id=1)
        self.assertEqual(record.question.question, self.question)

    def test_choise_correct_false(self):
        record = Choises.objects.get(option='Yes')
        self.assertTrue(record.correct)

    def test_choise_correct_true(self):
        record = Choises.objects.get(option='No')
        self.assertFalse(record.correct)
