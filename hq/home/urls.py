
from . import views
from django.urls import path, include



urlpatterns = [
    path('', views.home, name="home"),
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('profil', views.profil, name="profil"),
    path('pregledaj-belesku/<int:beleska_id>/', views.pregledaj_belesku, name="pregledaj_belesku"),
    path('izmeni-belesku/<int:beleska_id>/', views.izmeni_belesku, name="izmeni_belesku"),
    path('dodaj-belesku/', views.dodaj_belesku, name="dodaj_belesku"),
    path('obrisi_belesku/<int:beleska_id>/', views.obrisi_belesku, name="obrisi_belesku"),
    path('projekti/', views.projekti, name="projekti"),
    path('projekat/<int:projekat_id>/', views.projekat, name="projekat"),
    path('clanovi/', views.clanovi, name="clanovi"),
    path('webftp/', views.webftp, name="webftp"), 
    path('masine/', views.masine, name="masine"),
    path('pregledaj-masinu/<int:masina_id>/', views.pregledaj_masinu, name="pregledaj_masinu"),
    path('obrisi-masinu/<int:masina_id>/', views.obrisi_masinu, name="obrisi_masinu"),
    path('ai-copilot/', views.copilot, name="copilot"),
    path('planovi/', views.planovi, name="planovi"),
    path('obuka/', views.obuka, name="obuka"),
    
    
] 
