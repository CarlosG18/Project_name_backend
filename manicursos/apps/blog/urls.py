from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.NoticiaListView.as_view(), name="blog"),
]