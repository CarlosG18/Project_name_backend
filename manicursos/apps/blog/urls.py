from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoticiaListView.as_view(), name="index"),
]