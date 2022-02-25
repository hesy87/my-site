from django.shortcuts import render
from django.http import HttpResponse
from website.models import contact
from website.forms import Nameforms,contactform
from django.contrib import messages


def index_view (request) :
    return render(request,'website/index.html')

def about_view (request) :
    return render(request,'website/about.html')

def contact_view (request) :
    if request.method =='POST' :
        form=contactform(request.POST)
        if form.is_valid() : 
         form.save()  
         messages.success(request, 'Thank you')    
    form=contactform() 
    return render(request,'website/contact.html',{'form':form})

def test_view (request) :
    if request.method =='post' :
        form=contactform(request.POST)
        if form.is_valid :
            form.save()
            return HttpResponse('done')
        else :
            return HttpResponse('not done')

    form=contactform()
    return render(request,'test.html',{'form': form})         


