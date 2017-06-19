from django.db import models
from django.contrib.auth.models import User
'''Two models so far: Post and User (imported)'''

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