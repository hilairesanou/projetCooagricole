from django.db import models
from django.contrib.auth.models import User

class Membre(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Lien avec le modèle User de Django
    nom = models.CharField(max_length=100)  # Nom du membre
    prenom = models.CharField(max_length=100)  # Prénom du membre
    email = models.EmailField(unique=True)  # Adresse email unique
    phone_number = models.CharField(max_length=15)  # Numéro de téléphone
    date_inscription = models.DateField(auto_now_add=True)  # Date d'inscription automatique


    def __str__(self):
        return self.user.username
    def __str__(self):
        return f"{self.prenom} {self.nom}" 
