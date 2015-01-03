from django.test import TestCase
from polls.models import Polls, Questions, Answers
from users.models import CustomUser

from helper.utils import random_string


class PollTest(TestCase):

    def setUp(self):
        self.random_str = random_string()
        user_obj = CustomUser.objects.create_user(password='naglis',email='epasts@epasts.lv')
        obj = Polls.objects.create(user=user_obj,poll=self.random_str)
        obj.save()
        self.pk = obj.id

    def test_poll_creating(self):
        obj = Polls.objects.get(id=self.pk)
        self.assertEqual(obj.poll, self.random_str)


class QuestionTest(TestCase):
    def setUp(self):
        self.question = "5 x 5 is?"
        user_obj = CustomUser.objects.create_user(password='naglis',email='epasts@epasts.lv')
        poll = Polls.objects.create(user=user_obj,poll="test poll")
        question = Questions.objects.create(poll=poll, question=self.question)
        question.save()
        self.question_id = question.id

    def test_question_creating(self):
        obj = Questions.objects.get(id=self.question_id)
        self.assertEqual(obj.question, self.question)


class AnswersTest(TestCase):

    def setUp(self):

        user = CustomUser.objects.create_user(password='ivars', email='epasts@epasts.lv')
        Polls.objects.bulk_create([
            Polls(user=user, poll='cookie'),
            Polls(user=user, poll='muffin'),
            Polls(user=user, poll='pancake'),
        ])


