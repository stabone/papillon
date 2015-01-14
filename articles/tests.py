from django.test import TestCase

from users.models import CustomUser
from articles.models import Articles, ArticleReviews
from categories.models import Categories
from django.utils.unittest import skipIf


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

        super_user = CustomUser.objects.create_superuser(email='email@pasts.lv',
                                            password='super_password',
                                            user_name='super_user_name',
                                            last_name='super_last_name')
        super_user.save()

        category = Categories.objects.create(title='abc')

        Articles.objects.bulk_create([
            Articles(user=self.user, category=category,
                    title=self.title, embeded=self.embeded,
                    description=self.description),
            Articles(user=self.user, category=category,
                    title=self.title+'second', embeded=self.embeded,
                    description=self.description),
        ])

        ArticleReviews.objects.bulk_create([
            ArticleReviews(author=self.user, review_user=super_user,
                        article=Articles.objects.get(id=1)),
            ArticleReviews(author=self.user, review_user=super_user,
                        accept=True, article=Articles.objects.get(id=2)),
        ])

    def test_create_article(self):
        article = Articles.objects.get(id=1)

        self.assertEqual('Test Article', article.title)

    def test_hidden_new_article(self):
        article = Articles.objects.get(id=1)

        self.assertFalse(article.post, 'Hide new articles')

    def test_create_article_review(self):
        article_reviews = ArticleReviews.objects.all()

        self.assertEqual(article_reviews.count(), 2, 'Review count for now 2')

    # @skipIf(True)
    def test_if_negative_review(self):
        article_review = ArticleReviews.objects.get(id=1)

        self.assertFalse(article_review.accept, msg='This review should be negative')

    def test_if_positive_review(self):
        article_review = ArticleReviews.objects.get(id=2)

        self.assertTrue(article_review.accept, msg='This review should be positive')

