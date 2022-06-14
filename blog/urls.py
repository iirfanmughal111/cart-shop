from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path
from . import views


urlpatterns = [
   path("",views.index,name='blogHome'),
   path('blogview/<int:myid>',views.blogview,name='blogview'),
   path('contact',views.contact,name='contact'),
   path('archive/<str:cat>',views.archive,name='archive'),
   path('basicdata',views.basicData,name= 'basicdata'),



]