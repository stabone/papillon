from django.test import TestCase
from django.conf import settings

from badges.models import Badges, BadgeUser
from users.models import CustomUser


class BadgeTest(TestCase):

    def setUp(self):
        self.title = 'cool'
        Badges.objects.create(title=self.title)

    def test_badge_creating(self):
        badge = Badges.objects.get(id=1)
        self.assertEqual(badge.title, self.title)


class UserBadgeTest(TestCase):
    def setUp(self):
        self.title = 'cool'
        self.user = CustomUser.objects.create_user(
                                            password='password',
                                            email='epasts@epasts.lv')
        self.user.save()

        badge = Badges.objects.create(title=self.title)
        BadgeUser.objects.create(badge=badge, user=self.user)

    def test_record_exists(self):
        user_badges = BadgeUser.objects.filter(user=self.user)
        self.assertEqual(user_badges.count(), 1)

    def test_badge_desnt_exists(self):
        with self.assertRaises(Badges.DoesNotExist):
            Badges.objects.get(title='a'.join(self.title))

    def test_cool_badge(self):
        badge = Badges.objects.get(id=1)
        self.assertEqual(badge.title, self.title)


