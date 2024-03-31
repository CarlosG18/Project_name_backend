from django.urls import path
from . import views

urlpatterns = [
    path('', views.CursoListView.as_view(), name="index"),
]