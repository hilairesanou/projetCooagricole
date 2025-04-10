from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ModuleFormation, Module, Quizz, Question, Choix
from .models import Formation, InscriptionFormation
from django.contrib import messages

# Vue pour afficher la liste des formations
def liste_formations(request):
    formations = ModuleFormation.objects.all()
    return render(request, 'liste_formations.html', {'formations': formations})

def liste_formations(request):
    """Affiche la liste des formations disponibles."""
    formations = Formation.objects.all()
    return render(request, 'liste_formations.html', {'formations': formations})

def souscrire_formation(request, formation_id):
    """Permet à un membre de souscrire à une formation."""
    if request.user.is_authenticated and hasattr(request.user, 'membre'):
        formation = get_object_or_404(Formation, id=formation_id)
        InscriptionFormation.objects.create(membre=request.user.membre, formation=formation)
        messages.success(request, f"Vous êtes inscrit à la formation {formation.titre}.")
        return redirect('formation:liste_formations')
    else:
        messages.error(request, "Vous devez être connecté pour souscrire à une formation.")
        return redirect('login')  # Redirige vers la page de connexion si l'utilisateur n'est pas connecté    

# Vue pour afficher les détails d'une formation
def details_formation(request, formation_id):
    formation = get_object_or_404(ModuleFormation, id=formation_id)
    modules = formation.module_set.all()
    return render(request, 'details_formation.html', {'formation': formation, 'modules': modules})

# Vue pour afficher les détails d'un module
def details_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    return render(request, 'details_module.html', {'module': module})

# Vue pour afficher la liste des quiz disponibles
def liste_quizz(request):
    quizz_list = Quizz.objects.all()
    return render(request, 'liste_quizz.html', {'quizz_list': quizz_list})

# Vue pour afficher les détails d'un quiz et permettre à l'utilisateur de répondre aux questions
def detail_quizz(request, quizz_id):
    quizz = get_object_or_404(Quizz, id=quizz_id)
    questions = quizz.question_set.all()  # Note : Assurez-vous que les questions sont correctement reliées

    if request.method == 'POST':
        score = 0
        total_questions = questions.count()

        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                selected_choice = question.choix_set.get(id=selected_choice_id)  # Vérifier les choix
                if selected_choice.est_correct:
                    score += 1

        return HttpResponse(f'Votre score : {score}/{total_questions}')

    return render(request, 'formation/quizz/quizz_detail.html', {'quizz': quizz, 'questions': questions})
