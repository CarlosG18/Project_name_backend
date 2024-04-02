from django.urls import path
from . import views

app_name = 'curso'
urlpatterns = [
    path('cursos/', views.CursoListView.as_view(), name="cursos"),
    path('home/', views.home, name="home"),
]