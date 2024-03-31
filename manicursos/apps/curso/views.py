from django.shortcuts import render
from django.views import generic
from .models import Curso

class CursoListView(generic.ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "curso/cursos.html"
    paginate_by = 10

