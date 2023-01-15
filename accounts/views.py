from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import *

from django.contrib import messages



#static pages 
def about(request):
    context={}
    return render(request, 'accounts/about.html', context)

def english(request):
    context={}
    return render(request, 'accounts/english.html', context)

def rulesandtimeline(request):
    context={}
    return render(request, 'accounts/rules-and-timeline.html', context)

def plan(request):
    context={}
    return render(request, 'accounts/plan.html', context)

def table(request):
    context={}
    return render(request, 'accounts/table.html', context)

def arduinoide(request):
    context={}
    return render(request, 'accounts/arduinoide.html', context)

def electricity(request):
    context={}
    return render(request, 'accounts/electricity.html', context)

def digitaloutput(request):
    context={}
    return render(request, 'accounts/digitaloutput.html', context)

def balilar(request):
    context={}
    return render(request, 'accounts/balilar.html', context)
# end of static pages 



#dynamic pages

def ListBlog(request):
 
 
    return render(request,"accounts/index.html" )
"""
def DetailBlog(request,id):
    obj=get_object_or_404(Myblog, id=id)
    return render(request,"accounts/blog-single.html", {"detail":obj})


def home(request):
    context={}
    return render(request, 'accounts/index.html', context)

"""
 
 
 
 # the intro and lesson pages are here , copy this to add a new 'lesson' page
 
 
def introduction(request):
    
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        city= request.POST.get('city')
        body= request.POST.get('body')
        
        en = comment(name=name,comment_body=body,email=email,city=city)
        en.save()
        messages.success(request, "Comment added")
         
    
    Comment_list= comment.objects.all()
    
     
    return render(request, 'accounts/blog-single.html', {'Comment_list':Comment_list}) 


 


def firstclass(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        city= request.POST.get('city')
        body= request.POST.get('body')
        
        en = comment1(name=name,comment_body=body,email=email,city=city)
        en.save()
         
    
    Comment_list= comment1.objects.all()
    return render(request, 'accounts/firstclass.html', {'Comment_list':Comment_list})




def secondclass(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        city= request.POST.get('city')
        body= request.POST.get('body')
        
        en = comment2(name=name,comment_body=body,email=email,city=city)
        en.save()
         
    
    Comment_list= comment2.objects.all()
    return render(request, 'accounts/secondclass.html',  {'Comment_list':Comment_list})


def thirdclass(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        city= request.POST.get('city')
        body= request.POST.get('body')
      #change the comment number below and in comment_list  
        en = comment3(name=name,comment_body=body,email=email,city=city)
        en.save()
         
    
    Comment_list= comment3.objects.all()
    return render(request, 'accounts/thirdclass.html',  {'Comment_list':Comment_list})


def fourthclass(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        city= request.POST.get('city')
        body= request.POST.get('body')
      #change the comment number below and in comment_list  
        en = comment4(name=name,comment_body=body,email=email,city=city)
        en.save()
             
    Comment_list= comment4.objects.all()
    return render(request, 'accounts/fourthclass.html',  {'Comment_list':Comment_list})

def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        city= request.POST.get('city')
        body= request.POST.get('body')
      #change the comment number below and in comment_list  
        en = comment5(name=name,comment_body=body,email=email,city=city)
        en.save()
             
    Comment_list= comment5.objects.all()
    return render(request, 'accounts/contact.html',  {'Comment_list':Comment_list})

def birinjiders(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        city= request.POST.get('city')
        body= request.POST.get('body')
      #change the comment number below and in comment_list  
        en = comment6(name=name,comment_body=body,email=email,city=city)
        en.save()
             
    Comment_list= comment6.objects.all()
    #pdf = get_object_or_404(MyModel, pk=pdf_id)
    return render(request, 'accounts/birinji-ders.html',  {'Comment_list':Comment_list})    



