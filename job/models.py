from __future__ import unicode_literals

from django.db import models

# Create your models here.

# To use it at filter by ville
class Ville(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

# Service means catecory of servivces : exemples electicite, plamberie ..
class Service(models.Model):
    name = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='upload/')
    about = models.TextField()

    def __str__(self):
        return str(self.name)

# class Worker
class Worker(models.Model):
    cin = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    work = models.ForeignKey(Service, on_delete=models.CASCADE)
    city = models.ForeignKey(Ville, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='upload/')

    def __str__(self):
        return str(self.cin)


#class Work mean contra beetwen client and Worker
class Work(models.Model):
    pass





