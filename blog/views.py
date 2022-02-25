from ast import LtE
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.admin import postadmin
from blog.models import Post, commnet
import datetime
from django.db.models import F
from blog.forms import commentform

# Create your views here.
def blog_view (request,author_username=None) :
    posts = Post.objects.filter(status=1, published_date__lte = datetime.datetime.now())
    if author_username :
        posts = posts.filter(Author__username=author_username)
    context = {'posts':posts}
    return render (request , 'blog/blog-home.html',context)



def blog_single (request,pid, *args, **kwagrs):
    if request.method == "GET":
        Post.objects.filter(id=pid).update(conted_view=F('conted_view') + 1)  
    posts = Post.objects.filter(status=1, published_date__lte = datetime.datetime.now())
    post = get_object_or_404(posts , pk=pid)
    comments = commnet.objects.filter(post = post.id,approach=True).order_by('-created_date')
    form = commentform()
    context = {'posts':post,'comments':comments,'form':form}
    
    return render (request , 'blog/blog-single.html',context)

def test (request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render (request , 'test.html',context) 

def blog_category (request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render (request , 'blog/blog-home.html',context) 

def blog_search (request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET' :
       posts = posts.filter(content__contains=request.GET.get('s'))
    context = {'posts':posts}
    return render (request , 'blog/blog-home.html',context)
     

#def blog_single2 (request,pid):
    #if request.method == "GET":
        #Post.objects.filter(id=pid).update()  
   # posts2 = Post.objects.filter(status=1, published_date__lte = datetime.datetime.now(),id=F('id') - 1)
    #post2 = get_object_or_404(posts2 , pk=pid)
    #context2 = {'posts2':post2}
  #  return render (request , 'blog/blog-single.html',posts2)

