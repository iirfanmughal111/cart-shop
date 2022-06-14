from django.contrib import admin
from . models import comments, post
# Register your models here.
admin.site.register(post)
admin.site.register(comments)
# admin.site.register(featured)