from django.db import models
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Curso(models.Model):
    #definindo alguns choices
    NIVEL_CHOICES = {
        "1": "superior",
        "2": "técnico",
    }
    MODALIDADE_CHOICES = {
        "1": "presencial",
        "2": "semipresencial",
        "3": "online",
    }
    AREA_CHOICES = {
        "1": "Ciências Humanas",
        "2": "Ciências Exatas",
        "3": "Biociências",
    }
    
    #definindo os campos do modelo
    nome = models.CharField(max_length=200)
    nota = models.DecimalField(max_digits=2, decimal_places=1, blank=True, default=0.00)
    nivel = models.IntegerField(choices=NIVEL_CHOICES)
    modalidade = models.IntegerField(choices=MODALIDADE_CHOICES)
    carga_horaria = models.IntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="cursos/")
    preco = models.DecimalField(max_digits=7, decimal_places=3)
    area = models.IntegerField(choices=AREA_CHOICES)

    @property
    def atualizar_media(self):
        media = self.avaliacao_set.aggregate(media=Avg('nota'))['media']
        self.nota = media
        self.save()

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    STATUS_CHOICES = {
        "1": "formado",
        "2": "cursando",
    }
    #definindo os campos do modelo
    nome = models.CharField(max_length=200)
    curso = models.ManyToManyField(Curso)
    status = models.IntegerField(choices=STATUS_CHOICES)
    data_entrada = models.DateField()
    data_saida = models.DateField(blank=True, null=True)
    imagem = models.ImageField(upload_to="cursos/alunos/")

    def save(self, *args, **kwargs):
        if self.status == 1 and not self.data_saida:
            raise ValueError('data de saida é obrigatória para alunos formados!')
        super().save(*args,**kwargs)

    def __str__(self):
        return self.nome
    
class Professor(models.Model):
    TITULACAO_CHOICES = {
        "1": "doutor",
        "2": "mestre",
    }
    nome = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulacao = models.IntegerField(choices=TITULACAO_CHOICES)
    imagem = imagem = models.ImageField(upload_to="cursos/professores/")

    def __str__(self):
        return f'{self.nome} - {self.titulacao}'

class Avaliacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=2,decimal_places=1)
    comentario = models.TextField()

    def __str__(self):
        return f'curso = {self.curso.nome} - nota ({self.nota})'

@receiver(post_save, sender=Avaliacao)
def atualizar_media_curso(sender, instance, **kwargs):
    instance.curso.atualizar_media