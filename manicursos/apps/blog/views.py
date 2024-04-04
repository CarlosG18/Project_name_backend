from django.shortcuts import render
from django.views import generic
from .models import Noticia, Contato
from .forms import FormContato
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

class NoticiaListView(generic.ListView):
    model = Noticia
    template_name = "blog/noticias.html"
    context_object_name = "noticias"
    paginate_by = 6

def detail_noticia(request, id):
    noticia = Noticia.objects.get(id=id)
    
    return render(request, "blog/detail_noticia.html", {
        "noticia": noticia,
    })
      
def contato(request):
    if request.method == "POST":
        form_contato = FormContato(request.POST)
        if form_contato.is_valid():
            assunto = form_contato.cleaned_data["assunto"]
            email = form_contato.cleaned_data["email"]
            nome_usuario = form_contato.cleaned_data["nome"]
            mensagem = f"caro {nome_usuario}, \n seu email com assunto {assunto} será repondido em breve..."
            send_mail(
                assunto,
                mensagem,
                settings.EMAIL_HOST_USER,  # Email remetente
                [email],  # Lista de destinatários
                fail_silently=False,
            )
            contato = Contato(assunto=assunto,nome=nome_usuario,email=email,mensagem=form_contato.cleaned_data["mensagem"])
            contato.save()
        return HttpResponseRedirect(reverse('blog:contato'))
    else:
        form_contato = FormContato()    
    return render(request, "blog/contato.html", {
        "form_contato": form_contato,
    })