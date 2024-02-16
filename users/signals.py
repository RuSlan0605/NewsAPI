from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from .models import Profile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
        )

@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.first_name
        user.username = profile.username
        user.email = profile.email
        user.save()

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass

# post_save.connect(create_profile, sender=settings.AUTH_USER_MODEL)
# post_save.connect(update_user, sender=Profile)
# post_delete.connect(delete_user, sender=Profile)