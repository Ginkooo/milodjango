from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
import random

class User(AbstractUser):

    def gen_random():
        '''
        Returns random integer within rande <1, 100>
        '''

        return random.randint(1, 100)

    birthday = models.DateField()
    number = models.IntegerField(default=gen_random, validators=[MinValueValidator(1), MaxValueValidator(100)])

