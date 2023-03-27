from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ListBlog, name="home"),
   
   
    path('about/', views.about, name="about"),
    path('plan/', views.plan, name="plan"),
    path('table/', views.table, name="table"),
    path('arduino-ide/', views.arduinoide, name="arduino-ide"),
    
    path('english/', views.english, name="english"),
    path('electricity/', views.electricity, name="electricity"),
    path('digitaloutput/', views.digitaloutput, name="digitaloutput"),
    path('rules-and-timeline/', views.rulesandtimeline, name="rules-and-timeline"),
    path('balilar/', views.balilar, name="balilar"),
    path('special-class-one/', views.specialpageone, name="special-class-one"),
    path('google-classroom/', views.google_classroom, name="google_classroom"),
    
    
   ###########################end of static pages 
    
    
    path('introduction/', views.introduction, name="introduction"),
    path('tinkercad/', views.firstclass, name="first-class"),
    path('programming-basics/', views.secondclass, name="second-class"),
    path('third-class/', views.thirdclass, name="third-class"),
    path('fourth-class/', views.fourthclass, name="fourth-class"),
    path('contact/', views.contact, name="contact"),
    
    path('birinji-ders/', views.birinjiders, name="birinji-ders"),
    path('ikkinji-ders/', views.ikkinjiders, name="ikkinji-ders"),
    path('uchinji-ders/', views.uchinjiders, name="uchinji-ders"),
    path('totinji-ders/', views.totinjiders, name="totinji-ders"),
    path('bashinji-ders/', views.bashinjiders, name="bashinji-ders"),
    path('altinji-ders/', views.altinjiders, name="altinji-ders"),
    path('yettinji-ders/', views.yettinjiders, name="yettinji-ders"),
    path('sekkizinji-ders/', views.sekkizinjiders, name="sekkizinji-ders"),
    path('toqquzinji-ders/', views.toqquzinjiders, name="toqquzinji-ders"),
    path('oninji-ders/', views.oninjiders, name="oninji-ders"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


""" path('blog/<id>',views.DetailBlog, name="detail") """