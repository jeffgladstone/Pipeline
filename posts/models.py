from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    message = models.CharField(max_length=100)
    post_date = models.DateTimeField()
    user = models.ForeignKey(User, null = True, blank = True)
    votes = models.IntegerField()

    def __str__(self):
        return self.message