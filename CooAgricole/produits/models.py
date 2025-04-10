from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return self.nom

class Payment(models.Model):
    membre = models.ForeignKey('membres.Membre', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} by {self.membre} via Orange Money"

class Commande(models.Model):
    membre = models.ForeignKey('membres.Membre', on_delete=models.CASCADE)
    produit = models.ForeignKey('produits.Produit', on_delete=models.CASCADE, related_name='commandes_produits')
    quantite = models.PositiveIntegerField()
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande de {self.quantite} x {self.produit.nom} par {self.membre}"
