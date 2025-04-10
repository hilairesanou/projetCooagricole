from django.db import models
from membres.models import Membre


class Formation(models.Model):
    titre = models.CharField(max_length=100)  # Titre de la formation
    description = models.TextField()  # Description de la formation
    date_debut = models.DateField()  # Date de début de la formation
    date_fin = models.DateField()  # Date de fin de la formation
    prix = models.DecimalField(max_digits=10, decimal_places=2)  # Prix de la formation

    def __str__(self):
        return self.titre

class InscriptionFormation(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)  # Membre inscrit
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)  # Formation choisie
    date_inscription = models.DateTimeField(auto_now_add=True)  # Date d'inscription

    def __str__(self):
        return f"{self.membre} inscrit à {self.formation}"

class ModuleFormation(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.titre

class Module(models.Model):
    module_formation = models.ForeignKey(ModuleFormation, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    contenu = models.TextField()

    def __str__(self):
        return self.titre

class Question(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    texte = models.TextField()

    def __str__(self):
        return self.texte

class Choix(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    texte = models.CharField(max_length=200)
    est_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.texte

class Quizz(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.titre
