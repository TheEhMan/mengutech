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
    
    
   ###########################end of static pages 
    
    
    path('introduction/', views.introduction, name="introduction"),
 
    
    path('first-class/', views.firstclass, name="first-class"),
    path('second-class/', views.secondclass, name="second-class"),
    path('third-class/', views.thirdclass, name="third-class"),
    path('fourth-class/', views.fourthclass, name="fourth-class"),
    path('contact/', views.contact, name="contact"),
  
    
    







] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


""" path('blog/<id>',views.DetailBlog, name="detail") """