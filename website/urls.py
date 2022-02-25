from django.contrib import admin
from django.urls import path
from website.views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'website'
urlpatterns = [ 
path('admin/', admin.site.urls),
path('',index_view,name='index'),
path('about',about_view,name ='about'),
path('contact',contact_view,name ='contact'),
path('test',test_view,name ='test'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 


