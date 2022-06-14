from datetime import datetime
import imp
from pickle import TRUE
from tkinter.tix import Tree
from unicodedata import category
from xml.dom.expatbuilder import parseString
from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.http import HttpResponse
from requests import request
import requests
from . models import comments, post
from django.core.paginator import Paginator,EmptyPage

# Create your views here.

def index(request):
    # Getting All Posts
    get_db_post = post.objects.all()
    # Getting stared posts ids
    star_id=[]
    feature_id =[]
    # non_feature = []
    for blog in get_db_post:
        if (blog.blog_star==True):
            star_id.append(blog.blog_id)
        if (blog.blog_featured==True):
            feature_id.append(blog.blog_id)   

    # Getting last 5 stared posts
    first = post.objects.get(blog_id =star_id[-1])
    second = post.objects.get(blog_id =star_id[-2])
    third = post.objects.get(blog_id =star_id[-3])
    fourth = post.objects.get(blog_id =star_id[-4])
    fifth = post.objects.get(blog_id =star_id[-5])


    last_featured = post.objects.get(blog_id = feature_id[-1])
    
    # Pagination
    rev_posts = post.objects.all().order_by('-blog_id')
    page = Paginator(rev_posts,5)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)    



    dictionary = {
        'first':first,
        'second':second,
        'third':third,
        'fourth':fourth,
        'fifth':fifth,
        'last_featured':last_featured,
        'allposts':page,
       

    }

    
  
    return render(request,'blog/index.html',dictionary)





def blogview(request,myid):

    # Popular Posts
    get_db_post = post.objects.all()
    star_id=[]
    for blog in get_db_post:
        if (blog.blog_star==True):
            star_id.append(blog.blog_id)
    first = post.objects.get(blog_id =star_id[-1])
    second = post.objects.get(blog_id =star_id[-2])
    third = post.objects.get(blog_id =star_id[-3])
    fourth = post.objects.get(blog_id =star_id[-4])
    fifth = post.objects.get(blog_id =star_id[-5])

    # single Blog for blog view
    newblog = post.objects.get(blog_id = myid)

    #Other posts of same category

    blog_cat = newblog.blog_category
    same_cat_blogs = post.objects.filter(blog_category = blog_cat)
    cat_id= []
    for cat in same_cat_blogs:
        cat_id.append(cat.blog_id)
    s_cat1 = post.objects.get(blog_id=cat_id[-1])
    s_cat2 = post.objects.get(blog_id=cat_id[-2])
    s_cat3 = post.objects.get(blog_id=cat_id[-3])

    # Comments for specific post
    post_comment = comments.objects.filter(post_id = myid) 
  
    #context
    dictionary = {
        'first':first,
        'second':second,
        'third':third,
        'fourth':fourth,
        'fifth':fifth,
        'singleBlog':newblog,
        's_cat1':s_cat1,
        's_cat2':s_cat2,
        's_cat3':s_cat3,

        'post_comments':post_comment,

    }

    
    return render(request,'blog/blogview.html',dictionary)


def postcomments(request):
   
    if request.method =='POST':
        djname = request.POST.get('f_name','')
        djemail = request.POST.get('f_email','')
        djmsg = request.POST.get('f_msg','')
        djpost = request.POST.get('f_post','')
        comment = comments( post = djpost,c_name=djname,c_email= djemail, c_msg= djmsg,)
        comment.save()

def archive(request,cat):

    # Popular Posts
    get_db_post = post.objects.all()
    star_id=[]
    for blog in get_db_post:
        if (blog.blog_star==True):
            star_id.append(blog.blog_id)
    first = post.objects.get(blog_id =star_id[-1])
    second = post.objects.get(blog_id =star_id[-2])
    third = post.objects.get(blog_id =star_id[-3])
    fourth = post.objects.get(blog_id =star_id[-4])
    fifth = post.objects.get(blog_id =star_id[-5])

    posts = post.objects.filter( blog_category = cat)





    dictionary = {
        'first':first,
        'second':second,
        'third':third,
        'fourth':fourth,
        'fifth':fifth,
        'allcatblogs':posts,

    }

    return render(request,'blog/archive.html',dictionary)

# def comments(request):
#     return render(request,)


def login(request):

    return render(request,'login.html')


    
def contact(request):
    
   r = requests.get('https://api.thingspeak.com/channels/1751503/fields/1.json?results=2').json()
   d = {'r':r}
   return render(request,'blog/contact.html',r)




def basicData(request):
    get_db_post = post.objects.all()
    star_id=[]
    for blog in get_db_post:
        if (blog.blog_star==True):
            star_id.append(blog.blog_id)
    print(star_id)        
    first  = post.objects.get(blog_id = star_id[-1])
    second = post.objects.get(blog_id = star_id[-2])
    third  = post.objects.get(blog_id = star_id[-3])
    fourth = post.objects.get(blog_id = star_id[-4])
    fifth  = post.objects.get(blog_id = star_id[-5])
    dictionary = {
        'first':first,
        'second':second,
        'third':third,
        'fourth':fourth,
        'fifth':fifth,

    }
    return render(request,'blog/basic.html',dictionary)  