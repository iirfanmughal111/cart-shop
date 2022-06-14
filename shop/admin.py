from django.contrib import admin
from numpy import product

from .models import product
from .models import Contact
# Register your models here.

admin.site.register(product)
admin.site.register(Contact)