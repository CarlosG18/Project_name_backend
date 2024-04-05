from django.shortcuts import render
from django.views import generic
from .models import Curso, Aluno, Professor

def home(request):
  #retornar os cursos (3) que possuiem a nota maior
  cursos = Curso.objects.all().order_by('nota')[len(Curso.objects.all())-3:]
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
  cursos_populares = Curso.objects.all().order_by('nota')[len(Curso.objects.all())-3:]
  cursos_humanas = Curso.objects.filter(area=1)[:4]
  cursos_exatas = Curso.objects.filter(area=2)[:4]
  cursos_bio = Curso.objects.filter(area=3)[:4]
  alunos = Aluno.objects.all()
  return render(request, "curso/cursos.html", {
    "cursos_humanas": cursos_humanas,
    "cursos_exatas": cursos_exatas,
    "cursos_bio": cursos_bio,
    "cursos_populares": cursos_populares,
    "alunos": alunos,
  })
