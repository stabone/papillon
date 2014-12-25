from django.test import TestCase

from users.models import CustomUser
from articles.models import Articles
from categories.models import Categories


class ArticleTest(TestCase):

    def setUp(self):

        self.title = 'Test Article'
        self.embeded = """
            <iframe width=\"1280\" height=\"750\"
             src=\"//www.youtube.com/embed/9YqxNKxUIKA\" frameborder=\"0\" allowfullscreen></iframe>"""
        self.description = 'Just simple test case'

        self.user = CustomUser.objects.create_user(
                                            password='password',
                                            email='epasts@epasts.lv')
        self.user.save()
        category = Categories.objects.create(title='abc')

        article = Articles.objects.create(
                                    user=self.user,
                                    category=category,
                                    title=self.title,
                                    embeded=self.embeded,
                                    description=self.description)

        article.save()

    def test_create_article(self):
        article = Articles.objects.get(id=1)

        self.assertEqual('Test Article', article.title)

