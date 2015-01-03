from django.test import TestCase
from comments.models import MaterialComments, PollComments, ArticleComments
from polls.models import Polls
from articles.models import Articles
from categories.models import Categories
from users.models import CustomUser

from helper.utils import random_string


def get_user_object():
    return CustomUser.objects.create(
                                user_name='Ivars',
                                password='Naglis',
                                email='{}@epasts.lv'.format(random_string(max=10)))


class PollCommentsTest(TestCase):
    user_obj = get_user_object()

    def setUp(self):
        poll_obj = Polls.objects.create(user=self.user_obj,poll=random_string())
        obj = PollComments.objects.create(comment_author=get_user_object(),
                                        poll=poll_obj,
                                        comment=random_string(max=600))
        obj.save()
        self.pk = obj.id

    def test_comment_creation(self):
        obj = PollComments.objects.get(id=self.pk)
        self.assertEqual(obj.id, self.pk)


class ArticleCommentTests(TestCase):

    comment = 'unit test'
    user_obj = get_user_object()

    def setUp(self):
        category = Categories.objects.create(title='TEST')
        article  = Articles.objects.create(user=self.user_obj,
                                    category=category,
                                    title=random_string(max=255),
                                    description='just test',
                                    article='cookie')

        comment = ArticleComments.objects.create(comment_author=self.user_obj,
                                    article=article,
                                    comment=self.comment)
        comment.save()

    def test_create_comment(self):
        comment = ArticleComments.objects.get(comment_author=self.user_obj)
        self.assertEqual(comment.comment, self.comment)


