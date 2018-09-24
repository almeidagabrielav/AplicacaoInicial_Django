from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext
from coredrca.models import Aluno


def home(request):
    return render(request, "index.html")

def alunos(request, ):
    alunos = Aluno.objects.all() 
    context = {'alunos':alunos}
    return render(request, "alunos.html", context)