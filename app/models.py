from django.db import models

# Create your models here.


# ==========================================================
from django.contrib.auth.models import User
from django import forms


from db_file_storage.model_utils import delete_file, delete_file_if_needed
from django.db import models


class AppPicture(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)


class PortfolioAppPicture(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)


class Job(models.Model):
    name = models.CharField(max_length=100, unique=True)
    picture = models.ImageField(
        upload_to='app.AppPicture/bytes/filename/mimetype', blank=True, null=True)
    price = models.CharField(max_length=100, default="Не указано")
    info = models.TextField(default="Не указано")
    full_description = models.TextField(default="Не указано")

    def save(self, *args, **kwargs):
        delete_file_if_needed(self, 'picture')
        super(Job, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Job, self).delete(*args, **kwargs)
        delete_file(self, 'picture')

    def __str__(self):
        return self.name


class PortfolioCard(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(
        upload_to='app.AppPicture/bytes/filename/mimetype', blank=True, null=True)
    info = models.TextField()
    full_description = models.TextField(default="Не указано")

    def save(self, *args, **kwargs):
        delete_file_if_needed(self, 'picture')
        super(PortfolioCard, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(PortfolioCard, self).delete(*args, **kwargs)
        delete_file(self, 'picture')

    def __str__(self):
        return self.name


class Request(models.Model):
    phone = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.mail


class PortfolioPicture(models.Model):
    name = models.CharField(max_length=150, default="Не указано")
    picture = models.ImageField(
        upload_to='app.PortfolioAppPicture/bytes/filename/mimetype', blank=True, null=True)
    portfolio_job = models.ForeignKey(
        PortfolioCard, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=300)
    icon = models.CharField(max_length=300)
    text = models.TextField()

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(
        upload_to='app.AppPicture/bytes/filename/mimetype', blank=True, null=True)

    def __str__(self):
        return self.name


class UserProfileInfo(models.Model):
    is_doctor = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=80, default='Не указано')
    surname = models.CharField(max_length=80, default='Не указано')
    patronymic = models.CharField(max_length=80, default='Не указано')

    # portfolio_site = models.URLField(blank=True)
    # profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
# ==========================================================
