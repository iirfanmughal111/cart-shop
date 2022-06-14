from ast import Param
from heapq import nsmallest
from math import prod
import re
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from . models import product,Contact
from math import ceil
# Create your views here.

def index(request):

    allproducts = []
    catprods = product.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides= n//4 + ceil((n/4) + (n//4))
        allproducts.append([prod,range(1,nSlides),nSlides]) 
    
        



    params = {'allprods':allproducts}
    return render(request,"index.html", params)


def productview(request,myid):
    fetch_prod = product.objects.filter(id=myid)
    Param = {'product':fetch_prod[0]}
    return render(request,'productView.html',Param)
    

def checkout(request):
    return render(request,'checkout.html')



def search(request):
    return render(request,'search.html')



def contact(request):
    if request.method =='POST':
        djname = request.POST.get('name','')
        djemail = request.POST.get('email','')
        djphone = request.POST.get('phone','')
        djdesc = request.POST.get('desc','')
        contact = Contact(name=djname,email= djemail, phone= djphone, desc = djdesc)
        contact.save()



    return render(request,'contact.html')

def tracker(request):
    return render(request,'tracker.html')

def about(request):
    return render(request,'about.html')
    