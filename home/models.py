from django.db import models
from django.contrib.auth.models import User


class Images(models.Model):
  image = models.ImageField()


class Client(models.Model):

  name = models.ForeignKey(User, on_delete=models.CASCADE)
  age = models.IntegerField()
  image = models.ManyToManyField(Images)


class Doctor(models.Model):

  name = models.ForeignKey(User, on_delete=models.CASCADE)
  patient = models.ManyToManyField(Client)
  ph_no = models.IntegerField()