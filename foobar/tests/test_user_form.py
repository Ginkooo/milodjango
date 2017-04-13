from django.test import TestCase
from unittest.mock import MagicMock
from foobar.views import add_user, edit_user
from foobar.models import User
import sys

class UserActionTests(TestCase):

    def test_user_can_be_added(self):
        User.objects.all().delete()
        request = MagicMock()
        request.method = 'POST'
        request.POST = dict()
        request.POST['birthday'] = '02-02-2010'
        request.POST['username'] = 'bunny'
        request.POST['email'] = 'some@email.com'
        request.POST['password'] = 'strongpassword'
        request.POST['number'] = 25
        response = add_user(request)
        self.assertEqual(302, response.status_code)
        self.assertEqual(1, User.objects.all().count())

    def test_user_can_be_edited(self):
        User.objects.all().delete()
        user = User.objects.create(
                birthday='2011-02-02',
                username='ginko',
                password='somehash',
                email='other@email.com',
                )

        request = MagicMock()
        request.method = 'POST'
        request.POST = dict()
        request.POST['username'] = 'ginko'
        request.POST['password'] = 'somehash'
        request.POST['birthday'] = '02-02-2011'
        request.POST['email'] = 'example@email.com'
        response = edit_user(request, user.id)
        self.assertEqual(302, response.status_code)
        self.assertEqual('example@email.com', User.objects.all()[user.id].email)
        self.assertEqual(1, User.objects.all().count())
