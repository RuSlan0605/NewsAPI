from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):

    name = models.CharField(max_length=100, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='images/avatars/', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.username}'
    

class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status=Post.Status.TAYIN)

class Post(models.Model):

    class Status(models.TextChoices):
        TAYINEMES = 'TS', 'Tayin_emes'
        TAYIN = 'TN', 'Tayin'

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.TAYINEMES)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):

    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

    class Meta:

        ordering = ['created']
        verbose_name = 'Комменты'
        verbose_name_plural = 'Комментарий'











