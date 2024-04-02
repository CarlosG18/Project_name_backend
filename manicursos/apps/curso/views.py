from django.shortcuts import render
from django.views import generic
from .models import Curso, Aluno

class CursoListView(generic.ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "curso/cursos.html"
    paginate_by = 10

def home(request):
  #retornar os cursos (3) que possuiem a nota maior
  cursos = Curso.objects.all().order_by('nota')[:3]
  #retornar os 10 primeiros alunos
  alunos = Aluno.objects.all()[:10]
  return render(request, "curso/home.html", {
    "cursos": cursos,
    "alunos": alunos,
  })
