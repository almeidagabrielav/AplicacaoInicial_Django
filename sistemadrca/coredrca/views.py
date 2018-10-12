from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.template import RequestContext
from coredrca.models import Aluno, Curso, Disciplina
from .forms import AlunoForm
from django.db.models import Q


def home(request):
    return render(request, "index.html")

def obterAluno(request, alunoId):
    aluno = Aluno.objects.get(id=alunoId)
    context = { 'aluno':aluno}
    return render(request, 'alunos.html', context)

def alunos(request):
    alunos = Aluno.objects.all()

    filtro = request.GET.get('nomeBusca', None)
    if filtro:
        alunos = alunos.filter(Q(nome__icontains=filtro) | Q(matricula__icontains=filtro))

    context = {'alunos':alunos, 'filtro':filtro}

    return render(request, "alunos.html", context)

def editarAluno(request, alunoId):
    user = request.user
    aluno = Aluno.objects.get(id=alunoId)

    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno.nome=request.POST['nomeAtual']
            aluno.matricula=request.POST['matriculaAtual']
            aluno.save()
    
    alunos = Aluno.objects.all()
    context = { 'alunos':alunos}

    return render(request, 'alunos.html', context)

def excluirAluno(request, alunoId):
    aluno = Aluno.objects.get(id=alunoId)
    aluno.delete()
    alunos = Aluno.objects.all()
    context = { 'alunos':alunos}

    return render(request, 'alunos.html', context)

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
