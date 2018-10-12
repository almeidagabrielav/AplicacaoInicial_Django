from django.urls import path, include, re_path
from coredrca import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'alunos$', views.alunos, name='alunos'),
    re_path(r'salvarAluno$', views.salvarAluno, name='salvarAluno'),
    re_path(r'editarAluno/(?P<alunoId>\d{2})$', views.editarAluno, name='editarAluno'),
    re_path(r'excluirAluno/(?P<alunoId>\d{2})$', views.excluirAluno, name='excluirAluno'),
    re_path(r'obterAluno/(?P<alunoId>\d{2})$', views.obterAluno, name='obterAluno'),
]
