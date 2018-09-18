from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext
from coredrca.models import Aluno

def home(request):
    alunos = Aluno.objects.all()
    return render(request, "index.html")

def alunos(request):
    alunos = Aluno.objects.all()
    return render(request, "alunos.html", {'alunos':alunos})