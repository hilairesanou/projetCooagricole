from django.urls import path
from . import views

app_name = 'membres'  # Namespace pour l'application 'membres'

urlpatterns = [
    path('liste/', views.liste_membres, name='liste_membres'),  # Liste des membres
    path('', views.accueil, name='accueil'),  # Accueil
    path('ajouter/', views.ajouter_membre, name='ajouter_membre'),  # Ajouter un membre
    path('inscription/', views.inscription, name='inscription'),
]
