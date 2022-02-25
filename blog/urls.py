from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.views import *
from django.contrib import admin
from blog.feeds import LatestEntriesFeed


app_name = 'blog'
urlpatterns = [ 

path('',blog_view,name='index'),
path('<int:pid>',blog_single,name='single'),
path('category/<str:cat_name>',blog_category,name='category'),
path('tag/<str:tag_name>',blog_view,name='tag'),
path('author/<str:author_username>',blog_view,name='author'),
path('search/',blog_search,name='search'),
#path('<int:pid>',blog_single2,name='single2'),
path('rss/feed/', LatestEntriesFeed()),

]



