from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Commande
from produits.models import Produit

# Vue pour passer une commande
@login_required
def passer_commande(request, produit_id):
    produit = Produit.objects.get(id=produit_id)

    if request.method == 'POST':
        quantite = int(request.POST['quantite'])
        adresse_livraison = request.POST['adresse_livraison']

        # Créer la commande
        commande = Commande.objects.create(
            utilisateur=request.user,
            produit=produit,
            quantite=quantite,
            adresse_livraison=adresse_livraison
        )
        return redirect('commandes:confirmation', commande_id=commande.id)

    return render(request, 'passer_commande.html', {'produit': produit})

# Vue pour afficher la confirmation de commande
@login_required
def confirmation_commande(request, commande_id):
    commande = Commande.objects.get(id=commande_id)
    return render(request, 'confirmation.html', {'commande': commande})

# Vue pour vente en ligne
def vente_en_ligne(request):
    produits = Produit.objects.all()  # Assurez-vous que ce modèle existe dans l'application produits
    return render(request, 'commande.html', {'produits': produits})
