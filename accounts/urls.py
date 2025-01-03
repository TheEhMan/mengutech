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
    path('descriptionuy/', views.descriptionuy, name="descriptionuy"),
    path('description/', views.description, name="description"),
    
    
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
    path('onbirinji-ders/', views.onbirinjiders, name="onbirinji-ders"),
    path('onikkinji-ders/', views.onikkinjiders, name="onikkinji-ders"),
    path('onuchinji-ders/', views.onuchinjiders, name="onuchinji-ders"),
    path('ontotinji-ders/', views.ontotinjiders, name="ontotinji-ders"),
    path('onbashinji-ders/', views.onbashinjiders, name="onbashinji-ders"),
    path('onaltinji-ders/', views.onaltinjiders, name="onaltinji-ders"),
    path('onyettinji-ders/', views.onyettinjiders, name="onyettinji-ders"),
    path('onsekkizinji-ders/', views.onsekkizinjiders, name="onsekkizinji-ders"),
    path('ontoqquzinji-ders/', views.ontoqquzinjiders, name="ontoqquzinji-ders"),


    path('mengutech_second/', views.mengutech_second, name="mengutech_second"),
    path('mengutech_second_first/', views.second_first, name="second_first"),
    path('mengutech_second_seoncd/', views.second_second, name="second_second"),
    path('mengutech_second_third/', views.second_third, name="second_third"),
    path('mengutech_second_fourth/', views.second_fourth, name="second_fourth"),
    path('mengutech_second_fifth/', views.second_fifth, name="second_fifth"),
    path('mengutech_second_seventh/', views.second_seventh, name="second_seventh"),
    path('mengutech_second_eighth/', views.second_eighth, name="second_eighth"),
    path('mengutech_second_ninth/', views.second_ninth, name="second_ninth"),
    path('mengutech_second_tenth/', views.second_tenth, name="second_tenth"),
    path('mengutech_second_eleventh/', views.second_eleventh, name="second_eleventh"),
    path('mengutech_second_twelfth/', views.second_twelfth, name="second_twelfth"),
    path('mengutech_second_therteenth/', views.second_therteenth, name="second_therteenth"),
    

    path('bilimhumarlar/', views.bilimhumarlar_index, name="bilimhumarlar_index"),
    path('bilimhumarlar_contact/', views.bilimhumarlar_contact, name="bilimhumarlar_contact"),

    path('bilimhumarlar_anatil/', views.bilimhumarlar_anatil, name="bilimhumarlar_anatil"),
    path('bilimhumarlar_tajweed/', views.bilimhumarlar_tajweed, name="bilimhumarlar_tajweed"),
    path('bilimhumarlar_iman/', views.bilimhumarlar_iman, name="bilimhumarlar_iman"),
    path('bilimhumarlar_rohi_saghlamliq/', views.bilimhumarlar_rohi, name="bilimhumarlar_rohi"),
    path('bilimhumarlar_saghlamliq/', views.bilimhumarlar_saghlamliq, name="bilimhumarlar_saghlamliq"),
    path('bilimhumarlar_benglish/', views.bilimhumarlar_benglish, name="bilimhumarlar_benglish"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


""" path('blog/<id>',views.DetailBlog, name="detail") """