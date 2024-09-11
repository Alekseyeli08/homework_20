from django.contrib.auth.models import AbstractUser
from django.db import models
NULLABLE = {'blank': True, 'null': True}
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(**NULLABLE, upload_to='users/avatars/', verbose_name='аватар')
    phone = models.CharField(**NULLABLE, max_length=40, verbose_name='номер телефона')
    country = models.CharField(**NULLABLE, max_length=50, verbose_name='страна')

    token = models.CharField(**NULLABLE, max_length=100, verbose_name='токен')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return self.email