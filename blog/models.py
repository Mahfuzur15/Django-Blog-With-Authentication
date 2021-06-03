from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class BlogList(models.Model):
    title = models.CharField(max_length=60)
    dtm = models.DateTimeField()
    aname = models.CharField(max_length=60)
    text = models.TextField(max_length=1024)

class Registration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    pnmbr = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.username
