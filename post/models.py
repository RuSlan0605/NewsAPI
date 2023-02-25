from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):

    name = models.CharField(max_length=45, blank=True, null=True)

class Calendar(models.Model):

    name = models.CharField(max_length=45, blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Календарь'
        verbose_name = 'Календарь'

class Event(models.Model):

    name = models.CharField(max_length=45, blank=True, null=True)
    location = models.CharField(max_length=45, blank=True, null=True)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Событие'
        verbose_name = 'Событии'

class Invitees(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
