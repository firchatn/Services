from __future__ import unicode_literals

from django.db import models

# Create your models here.

# To use it at filter by ville
class Ville(models.Model):
    pass

# Service means catecory of servivces : exemples electicite, plamberie ..
class Service(models.Model):
    name = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='upload/')
    about = models.TextField()

# class Worker
class Worker(models.Model):
    pass

#class Work mean contra beetwen client and Worker
class Work(models.Model):
    pass





