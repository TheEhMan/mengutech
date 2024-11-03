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

def specialpageone(request):
    context={}
    return render(request, 'accounts/specialclassone.html', context)

def google_classroom(request):
    context={}
    return render(request, 'accounts/google_classroom.html', context)

def mengutech_second(request):
    context={}
    return render(request, 'accounts/mengutech_second/mengutech_second.html', context)

def second_second(request):
    context={}
    return render(request, 'accounts/mengutech_second/second_second.html', context)

def second_third(request):
    context={}
    return render(request, 'accounts/mengutech_second/second_third.html', context)

def second_fourth(request):
    context={}
    return render(request, 'accounts/mengutech_second/second_fourth.html', context)

def second_fifth(request):
    context={}
    return render(request, 'accounts/mengutech_second/second_fifth.html', context)

def second_seventh(request):
    context={}
    return render(request, 'accounts/mengutech_second/second_seventh.html', context)

def second_eighth(request):
    context={}
    return render(request, 'accounts/mengutech_second/second_eighth.html', context)

def second_ninth(request):
    context={}
    return render(request, 'accounts/mengutech_second/second_ninth.html', context)

def second_tenth(request):
    context={}
    return render(request, 'accounts/mengutech_second/second_tenth.html', context)

def second_eleventh(request):
    context={}
    return render(request, 'accounts/mengutech_second/second_eleventh.html', context)

def second_twelfth(request):
    context={}
    return render(request, 'accounts/mengutech_second/second_twelfth.html', context)

def second_therteenth(request):
    context={}
    return render(request, 'accounts/mengutech_second/second_therteenth.html', context)

def second_first(request):
    #pdf = get_object_or_404(MyModel, pk=pdf_id)
    return render(request, 'accounts/mengutech_second/second_first.html', {})

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
    return render(request, 'accounts/blog-single.html', {}) 

def firstclass(request):
    return render(request, 'accounts/firstclass.html', {})

def secondclass(request):
    return render(request, 'accounts/secondclass.html',  {})

def thirdclass(request):
    return render(request, 'accounts/thirdclass.html',  {})

def fourthclass(request):
    return render(request, 'accounts/fourthclass.html',  {})

def contact(request):
    return render(request, 'accounts/contact.html',  {})

def birinjiders(request):
    return render(request, 'accounts/birinji-ders.html',  {})    

def ikkinjiders(request):
    return render(request, 'accounts/ikkinji-ders.html',  {})    

def uchinjiders(request):
    return render(request, 'accounts/uchinji-ders.html',  {})    

def totinjiders(request):
    return render(request, 'accounts/totinji-ders.html',  {})    

def bashinjiders(request):
    return render(request, 'accounts/bashinji-ders.html',  {})

def altinjiders(request):
    return render(request, 'accounts/altinji-ders.html',  {})

def yettinjiders(request):
    return render(request, 'accounts/yettinji-ders.html',  {})

def sekkizinjiders(request):   
    return render(request, 'accounts/sekkizinji-ders.html',  {})

def toqquzinjiders(request):
    return render(request, 'accounts/toqquzinji-ders.html',  {})

def oninjiders(request):
    return render(request, 'accounts/oninji-ders.html',  {})

def onbirinjiders(request):
    return render(request, 'accounts/onbirinji-ders.html',  {})

def onikkinjiders(request):
    return render(request, 'accounts/onikkinji-ders.html',  {})

def onuchinjiders(request):
    return render(request, 'accounts/onuchinji-ders.html',  {})

def ontotinjiders(request):
    return render(request, 'accounts/ontotinji-ders.html',  {})

def onbashinjiders(request):
    return render(request, 'accounts/onbashinji-ders.html',  {})

def onaltinjiders(request):
    return render(request, 'accounts/onaltinji-ders.html',  {})

def onyettinjiders(request):
    return render(request, 'accounts/onyettinji-ders.html',  {})

def onsekkizinjiders(request):
    return render(request, 'accounts/onsekkizinji-ders.html',  {})

def ontoqquzinjiders(request):
    return render(request, 'accounts/ontoqquzinji-ders.html',  {})

def description(request):
    return render(request, 'accounts/description.html',  {})

def descriptionuy(request):
    return render(request, 'accounts/descriptionuy.html',  {})

################Bilim Humarlar################
def bilimhumarlar_index(request):
    return render(request, 'accounts/bilimhumarlar/index.html',  {})

def bilimhumarlar_contact(request):
    return render(request, 'accounts/bilimhumarlar/contact.html',  {})

def bilimhumarlar_anatil(request):
    return render(request, 'accounts/bilimhumarlar/dersler/anatil.html',  {})

def bilimhumarlar_iman(request):
    return render(request, 'accounts/bilimhumarlar/dersler/iman.html',  {})

def bilimhumarlar_tajweed(request):
    return render(request, 'accounts/bilimhumarlar/dersler/tajweed.html',  {})

def bilimhumarlar_rohi(request):
    return render(request, 'accounts/bilimhumarlar/dersler/rohi.html',  {})

def bilimhumarlar_saghlamliq(request):
    return render(request, 'accounts/bilimhumarlar/dersler/saghlamliq.html',  {})

def bilimhumarlar_benglish(request):
    return render(request, 'accounts/bilimhumarlar/dersler/benglish.html',  {})