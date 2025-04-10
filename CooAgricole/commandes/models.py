from django.db import models
from produits.models import Produit  # Importer le modèle Produit
from django.contrib.auth.models import User  # Si tu utilises l'authentification

class Commande(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)  # Lien avec l'utilisateur
    produit = models.ForeignKey('produits.Produit', on_delete=models.CASCADE, related_name='commandes_commandes')
    quantite = models.PositiveIntegerField()
    date_commande = models.DateTimeField(auto_now_add=True)
    adresse_livraison = models.CharField(max_length=255)  # Adresse de livraison (optionnel mais utile)

    def __str__(self):
        return f"Commande de {self.utilisateur.username} pour {self.produit.nom}"
