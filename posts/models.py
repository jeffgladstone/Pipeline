from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    '''fields include message (String of characters), post_date (DateTime), User (Foreign Key because each post has only one User)
    votes (integer regarding amount)'''

    message = models.CharField(max_length=100)
    post_date = models.DateTimeField()
    user = models.ForeignKey(User, null = True, blank = True)
    votes = models.IntegerField()

    def __str__(self):
        '''Post model is always defaulted to display its message field'''
        return self.message

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()