from django.urls import path
from . import views

app_name = 'produits'

urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    path('ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('payer/', views.make_payment, name='make_payment'),
    path('success/', views.payment_success, name='payment_success'),
    path('passer_commande/<int:produit_id>/', views.passer_commande, name='passer_commande'),  # Vue pour passer une commande
]
