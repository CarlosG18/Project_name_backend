from django.urls import path
from . import views

app_name = 'curso'
urlpatterns = [
    path('cursos/', views.cursos, name="cursos"),
    path('home/', views.home, name="home"),
    path('sobre/', views.sobre, name="sobre"),
]