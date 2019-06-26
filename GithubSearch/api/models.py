from django.db import models
from django.db import models
# Create your models here.

class User(models.Model):

    login = models.CharField(max_length=20)
    avatar_url = models.CharField()
    url = models.CharField()
