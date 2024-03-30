from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300)
    criador = models.CharField(max_length=200)
    datatime_da_pub = models.DateTimeField(auto_now=True)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to="noticias/")

    def __str__(self):
        return self.titulo
