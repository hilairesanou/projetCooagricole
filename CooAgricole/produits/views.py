from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produit, Payment, Commande
from .forms import PaymentForm
from django.contrib import messages

def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'liste_produits.html', {'produits': produits})

def ajouter_produit(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        prix = request.POST.get('prix')
        quantite = request.POST.get('quantite')

        nouveau_produit = Produit(nom=nom, description=description, prix=prix, quantite=quantite)
        nouveau_produit.save()
        messages.success(request, "Le produit a été ajouté avec succès.")
        return redirect('produits:liste_produits')

    return render(request, 'ajouter_produit.html')
@login_required
def passer_commande(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == 'POST':
        quantite = int(request.POST.get('quantite'))

        if quantite > produit.quantite:
            messages.error(request, "Quantité demandée supérieure au stock disponible.")
            return redirect('produits:liste_produits')

        commande = Commande(membre=request.user.membre, produit=produit, quantite=quantite)
        commande.save()

        produit.quantite -= quantite
        produit.save()

        messages.success(request, "Votre commande a été passée avec succès.")
        return redirect('produits:liste_produits')
    
    return render(request, 'passer_commande.html', {'produit': produit})
@login_required
def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.member = request.user.membre
            payment.save()
            messages.success(request, "Votre paiement a été enregistré avec succès.")
            return redirect('produits:payment_success')
    else:
        form = PaymentForm()
    return render(request, 'make_payment.html', {'form': form})

def payment_success(request):
    return render(request, 'payment_success.html')
