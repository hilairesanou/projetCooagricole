from django.urls import path
from . import views

app_name = 'commandes'

urlpatterns = [
    path('vente/', views.vente_en_ligne, name='vente_en_ligne'),
    path('passer/<int:produit_id>/', views.passer_commande, name='passer_commande'),
    path('confirmation/<int:commande_id>/', views.confirmation_commande, name='confirmation'),
]
