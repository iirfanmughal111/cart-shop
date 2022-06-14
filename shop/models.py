from operator import mod
from unicodedata import category
from django.db import models
from matplotlib.pyplot import cla

# Create your models here.


class product(models.Model):
    product_id = models.AutoField
    product_title = models.CharField(max_length=50,default="")
    category = models.CharField(max_length=50,default="")
    Sub_category = models.CharField(max_length=50,default="")
    price = models.IntegerField(default="0")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.product_title


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70,default="")
    email = models.CharField(max_length=70,default="")
    phone = models.CharField(max_length=70,default="")
    desc = models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name



