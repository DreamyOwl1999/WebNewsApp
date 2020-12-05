from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class newsSection(models.Model):
    Profile = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True)
    choices = models.CharField(max_length = 1000)

class Article(models.Model):
    title = models.CharField(max_length = 1000)
    section = models.CharField(max_length = 1000)
    likes = models.PositiveIntegerField()
    writing = models.CharField(max_length = 100000)







# Create your models here.
