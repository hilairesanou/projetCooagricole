from django.shortcuts import render, redirect
from .models import Membre
from .forms import InscriptionForm
from django.contrib import messages

def liste_membres(request):
    """Affiche la liste de tous les membres."""
    membres = Membre.objects.all()
    return render(request, 'liste_membres.html', {'membres': membres})

def accueil(request):
    """Affiche la page d'accueil."""
    return render(request, 'accueil.html')  # Utilise le template 'accueil.html'

def ajouter_membre(request):
    """Ajoute un nouveau membre à la base de données."""
    if request.method == 'POST':
        nom = request.POST.get('nom')  # Récupère le champ 'nom'
        prenom = request.POST.get('prenom')  # Récupère le champ 'prenom'
        email = request.POST.get('email')  # Récupère le champ 'email'
        telephone = request.POST.get('telephone')  # Récupère le champ 'telephone'
        
        # Crée un nouveau membre avec les informations fournies
        nouveau_membre = Membre(nom=nom, prenom=prenom, email=email, telephone=telephone)
        nouveau_membre.save()
        return redirect('membres:liste_membres')  # Redirige vers la liste des membres

    return render(request, 'ajouter_membre.html')  # Charge le template 'ajouter_membre.html'

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Inscription réussie ! Vous êtes maintenant membre de la coopération.")
            return redirect('membres:accueil')
    else:
        form = InscriptionForm()
    return render(request, 'inscription.html', {'form': form})
