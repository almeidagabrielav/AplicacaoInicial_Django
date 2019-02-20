from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.template import RequestContext
from coredrca.models import Aluno, Curso, Disciplina
from .forms import AlunoForm
from django.db.models import Q
import coreapi, json, requests
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
    alunoCopia = aluno

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

    return render(request, 'alunos', {'form': form, 'alunos':alunos})

def listarTransacoes(request):
    user = request.user
    dados = {
        "Tabelas": [{
            "Atributos": [
            {
                "CampoAlterado": "ABC",
                "ValorInicial": "LU",
                "ValorFinal": "UL"
            }],
            "Nome": "TESTE",
            "Esquema": "AAT"            
        }],
        "TipoAlteracao": "UPDATE",
        "UsuarioId": "20",
        "Ip": "200219"
    }
    response = requests.post("http://localhost:8000/transacoes/", json = dados)
    print (response.status_code)
    print(response.content)
    context = { 'transacoes':response.content }
    return render(request, 'sismadServer.html', context)
