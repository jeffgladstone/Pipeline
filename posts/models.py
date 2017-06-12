from django.db import models

class Account(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    
    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Post(models.Model):
    message = models.CharField(max_length=100)
    post_date = models.DateTimeField()
    account= models.ForeignKey(Account)
    votes = models.IntegerField()

    def __str__(self):
        return self.message