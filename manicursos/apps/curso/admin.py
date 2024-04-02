from django.contrib import admin
from .models import Curso, Aluno, Professor, Avaliacao

# Register your models here.
admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Avaliacao)