from django.db import models


# Create your models here.
#superuser-famname
#keyqwerty12
class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
