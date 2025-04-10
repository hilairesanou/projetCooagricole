from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from membres import views  # Import de la vue accueil
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # URL de l'administration
    path('commandes/', include('commandes.urls')),  #  URLs de l'application 'commandes'
    path('membres/', include('membres.urls')),  # URLs de l'application Membres
    path('formation/', include('formation.urls')),  # URLs de l'application Formation
    path('produits/', include('produits.urls')),  # URLs pour les paiements (application Produits)
    path('', views.accueil, name='accueil'), 
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', include('django.contrib.auth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])