from distutils.archive_util import make_zipfile
from django.db import models
from numpy import true_divide

# Create your models here.


class post (models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length = 100, default="")
    blog_desc = models.CharField(max_length = 10000, default="")
    blog_category = models.CharField(max_length=50,default="")
    pub_date = models.DateField(auto_now_add=True)
    blog_star = models.BooleanField(default=False)
    blog_featured = models.BooleanField(default=False)
    blog_imgs = models.ImageField()

    def __str__(self):
        return self.blog_title


class comments(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    c_name = models.CharField(max_length = 50,default="") 
    c_email = models.CharField(max_length = 50,default="") 
    c_msg   = models.CharField(max_length = 500,default="") 
    c_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.c_name


