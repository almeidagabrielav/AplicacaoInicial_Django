from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.template import RequestContext
from coredrca.models import Aluno, Curso, Disciplina
from .forms import AlunoForm


def home(request):
    return render(request, "index.html")

def alunos(request):
    alunos = Aluno.objects.all()
    context = {'alunos':alunos}
    return render(request, "alunos.html", context)

def obterAluno(request, alunoId):
    aluno = Aluno.objects.get(id=alunoId)
    context = {'aluno':aluno}
    return render(request, 'modalVerAluno.html', context)

def salvarAluno(request):
    user = request.user
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = Aluno(
                nome=request.POST['nomeAtual'],
                matricula=request.POST['matriculaAtual']
            ) 
            aluno.save()
    
    alunos = Aluno.objects.all()

    return render(request, 'alunos.html', {'form': form, 'alunos':alunos})

def filtrarAluno(request, parametroFiltro):
    user = request.user
    alunos = Aluno.objects.get(nome=parametroFiltro)
    context = {'alunos':alunos}
    return render(request, 'alunos.html', context)