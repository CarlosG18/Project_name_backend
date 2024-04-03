from django.shortcuts import render
from django.views import generic
from .models import Curso, Aluno, Professor

def home(request):
  #retornar os cursos (3) que possuiem a nota maior
  cursos = Curso.objects.all().order_by('nota')[:3]
  #retornar os 10 primeiros alunos
  alunos = Aluno.objects.all()[:10]
  return render(request, "curso/home.html", {
    "cursos": cursos,
    "alunos": alunos,
  })

def sobre(request):
  professores = Professor.objects.all()
  return render(request, "curso/sobre.html", {
    "professores": professores,
  })

def cursos(request):
  cursos_populares = Curso.objects.all().order_by('nota')[:3]
  cursos = Curso.objects.all()
  alunos = Aluno.objects.all()
  return render(request, "curso/cursos.html", {
    "cursos": cursos,
    "cursos_populares": cursos_populares,
    "alunos": alunos,
  })
