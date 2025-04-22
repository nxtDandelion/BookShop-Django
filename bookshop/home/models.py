from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

COVER_TYPE = [
    ('HARD', 'Твердый переплет'),
    ('SOFT', 'Мягкий переплёт'),
    ('E', 'Электронная книга')
]


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    authors = models.CharField(max_length=200, verbose_name="Авторы")
    page_count = models.PositiveIntegerField(verbose_name="Количество страниц")
    cover_type = models.CharField(choices=COVER_TYPE, verbose_name="Тип переплёта")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    publication_date = models.DateField(verbose_name="Дата публикации")
    code = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class MyUser(AbstractBaseUser):
    login = models.CharField(unique=True, max_length=20, verbose_name="Логин")
    email = models.EmailField(unique=True, verbose_name="Почта")
    password = models.CharField(max_length=20, verbose_name="Пароль")
    birth_date = models.DateField(verbose_name="Дата рождения", blank=True, null=True)

    USERNAME_FIELD = 'login'
    objects = BaseUserManager()

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
