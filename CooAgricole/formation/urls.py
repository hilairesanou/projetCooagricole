from django.urls import path
from . import views

app_name = 'formation'  # Définition de l'espace de noms

urlpatterns = [
    path('<int:formation_id>/', views.details_formation, name='details_formation'),  # Détails d'une formation
    path('module/<int:module_id>/', views.details_module, name='details_module'),  # Détails d'un module
    path('quizz/', views.liste_quizz, name='liste_quizz'),  # Liste des quizz
    path('quizz/<int:quizz_id>/', views.detail_quizz, name='detail_quizz'),  # Détail d'un quizz
    path('souscrire/<int:formation_id>/', views.souscrire_formation, name='souscrire_formation'),  # Souscription à une formation
     path('', views.liste_formations, name='liste_formations'),  # Liste des formations
]
