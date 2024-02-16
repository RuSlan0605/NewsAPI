from django.db import models    
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify  
from django.conf import settings
    

class CustomUser(AbstractUser):

    name = models.CharField(max_length=100, blank=True, null=True, db_index=True, unique=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.username}'


class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True, db_index=True)
    first_name = models.CharField(max_length=50, 
        blank=True, null=True)
    last_name = models.CharField(max_length=50,
        blank=True, null=True)
    email = models.EmailField(max_length=50, 
        blank=True, null=True, unique=True)
    username = models.CharField(max_length=50, 
        blank=True, null=True, unique=True)
    avatar = models.ImageField(upload_to='images/avatars/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        return super(Profile, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user.username
    

