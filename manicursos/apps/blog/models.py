from django.db import models
from django.utils import timezone

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300)
    criador = models.CharField(max_length=200)
    datatime_da_pub = models.DateTimeField(auto_now=True)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to="noticias/")
    data = models.DateField(default=timezone.now)

    def __str__(self):
        return self.titulo

class Contato(models.Model):
    ASSUNTO_CHOICES = {
        "rec": "Reclamação",
        "duv": "Dúvidas",
        "cri": "Critica",
        "aju": "Ajuda",
        "out": "Outro",
    }
    
    assunto = models.CharField(max_length=3,choices=ASSUNTO_CHOICES)
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    mensagem = models.TextField() 

    def __str__(self):
        return f'assunto: {self.assunto} - {self.nome} - {self.email}'