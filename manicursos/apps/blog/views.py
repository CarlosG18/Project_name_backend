from django.shortcuts import render
from django.views import generic
from .models import Noticia

class NoticiaListView(generic.ListView):
    model = Noticia
    template_name = "blog/noticias.html"
    context_object_name = "noticias"
    paginate_by = 6