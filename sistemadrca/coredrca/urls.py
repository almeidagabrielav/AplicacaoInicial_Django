from django.urls import path, include, re_path
from coredrca import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'alunos$', views.alunos, name='alunos'),
]
