from django.contrib import admin
from .models import Curso, Aluno, Professor, AvaliacaoProf, AvaliacaoAluno

# Register your models here.
admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(AvaliacaoProf)
admin.site.register(AvaliacaoAluno)