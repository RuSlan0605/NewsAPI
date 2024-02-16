from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

class Category(models.Model):

    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)

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

    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    body = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.TAYINEMES)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-created']
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.title
    
    
class News(models.Model):

    title = models.CharField(max_length=100, db_index=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/news/', blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class Comment(models.Model):

    name = models.CharField(max_length=100, blank=True, db_index=True)
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











