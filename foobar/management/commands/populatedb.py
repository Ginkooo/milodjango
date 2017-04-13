from django.core.management import BaseCommand
from foobar.models import User

class Command(BaseCommand):

    help = 'Populates the database with some data'

    def handle(self, *args, **kwargs):
        users = []
        users.append(User(birthday='1995-12-09', username='ginko', email='some@email.com'))
        users.append(User(birthday='1992-12-09', username='ginkt', email='some@email.pl'))
        users.append(User(birthday='1993-12-09', username='ginkr', email='some@email.eu'))
        users.append(User(birthday='1991-12-09', username='ginke', email='some@email.mail'))
        users.append(User(birthday='1990-12-09', username='ginka', email='some@email.de'))
        for user in users:
            user.set_password('password')
            user.full_clean()
            user.save()
