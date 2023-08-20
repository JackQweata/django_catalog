from django.contrib.auth.models import AbstractUser
from django.db import models

BLANCNULL = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    phone = models.CharField('телефон', max_length=35)
    country = models.CharField('страна', max_length=50)
    avatar = models.ImageField('аватарка', upload_to='users/', **BLANCNULL)
    email = models.EmailField(verbose_name='почта', unique=True)
    token_reg = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
