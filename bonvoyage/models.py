from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Destination(models.Model):  # converting class as a model

    name = models.CharField(max_length=100)  # specify type of the column
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
