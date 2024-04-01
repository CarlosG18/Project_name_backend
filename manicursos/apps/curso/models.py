from django.db import models

# Create your models here.
class Curso(models.Model):
    #definindo alguns choices
    NIVEL_CHOICES = {
        1: "superior",
        2: "técnico",
    }
    MODALIDADE_CHOICES = {
        1: "presencial",
        2: "semipresencial",
        3: "online",
    }
    
    #definindo os campos do modelo
    nome = models.CharField(max_length=200)
    nivel = models.IntegerField(choices=NIVEL_CHOICES)
    modalidade = models.IntegerField(choices=MODALIDADE_CHOICES)
    carga_horaria = models.IntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="cursos/")

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    STATUS_CHOICES = {
        1: "formado",
        2: "cursando",
    }
    #definindo os campos do modelo
    nome = models.CharField(max_length=200)
    curso = models.ManyToManyField(Curso)
    status = models.IntegerField(choices=STATUS_CHOICES)
    data_entrada = models.DateField()
    data_saida = models.DateField(null=True)
    imagem = models.ImageField(upload_to="cursos/alunos/")

    def __str__(self):
        return self.nome
