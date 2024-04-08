from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.NoticiaListView.as_view(), name="blog"),
    path('noticia/<int:id>', views.detail_noticia, name="noticia"),
    path('contato/', views.contato, name="contato"),
]