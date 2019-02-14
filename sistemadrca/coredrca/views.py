from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.template import RequestContext
from coredrca.models import Aluno, Curso, Disciplina
from .forms import AlunoForm
from django.db.models import Q
import coreapi, json, requests

def listarTransacoes(request):
    user = request.user
    dados = data = {
        "TipoAlteracao": "update",
        "UsuarioId": "22",
        "Ip": "22aa",
        "Tabelas": [
        {
            "Nome": "Tab1",
            "Esquema": "aaa",
            "Atributos": [
            {
                "CampoAlterado": "xxx",
                "ValorInicial": "a",
                "ValorFinal": "b"
            }]
        },
        {
            "Nome": "Tab3",
            "Esquema": "aaa",
            "Atributos": [
            {
                "CampoAlterado": "xxx",
                "ValorInicial": "a",
                "ValorFinal": "b"
            },
            {
                "CampoAlterado": "aaa",
                "ValorInicial": "c",
                "ValorFinal": "d"
            }]
        }]
    }
    response = requests.post("http://localhost:7000/transacoes", data = dados)
    print (response.status_code)
    #print(response.content)
    #context = { 'transacoes':response.content }
    #return render(request, 'sismadServer.html', context)

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
    # client = coreapi.Client()
    # schema = client.get('http://127.0.0.1:8000/schema/')
    
    user = request.user
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = Aluno(
                nome=request.POST['nomeAtual'],
                matricula=request.POST['matriculaAtual']
            ) 
            aluno.save()

    # novaTransacao = client.action(schema, ['transacoes', 'create'], params={"TipoAlteracao":"Insert","UsuarioId":"3","Ip":"TesteIntegracao111"})
    
    alunos = Aluno.objects.all()

    return render(request, 'alunos', {'form': form, 'alunos':alunos})
