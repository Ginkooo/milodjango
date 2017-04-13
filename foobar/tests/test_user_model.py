from django.test import TestCase
from foobar.models import User
from datetime import date

class UserModelTests(TestCase):

    def setUp(self):
        User.objects.all().delete()
        user = User(birthday=date.today(), username='bunny')
        user.set_password('P455w0rd')
        user.save()

    def test_user_is_added_properly(self):
        self.assertEqual(1, User.objects.all().count())

    def test_adding_user_generate_random_number_beetween_1_and_100(self):
        rand_num = User.objects.all()[0].number
        self.assertTrue(rand_num in range(1, 101))
