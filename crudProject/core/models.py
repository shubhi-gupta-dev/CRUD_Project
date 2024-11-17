from django.db import models


# Create your models here.
class Product(models.Model):
    pname = models.CharField(max_length=60)
    pdesc = models.CharField(max_length=200)
    price = models.IntegerField()
    photo = models.ImageField(upload_to = "myimage")