from django.contrib import admin
from .models import ModuleFormation, Module, Quizz
from .models import Formation, InscriptionFormation

admin.site.register(ModuleFormation)
admin.site.register(Module)
admin.site.register(Quizz)
admin.site.register(Formation)
admin.site.register(InscriptionFormation)