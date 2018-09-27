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

# def criarAluno(request):
#     form = ProductForm(request.POST or None)
#     cursos = Curso.objects.all()
#     disciplinas = Disciplina.objects.all()

#     if form.is_valid():
#         form.save()
#         return redirect('alunos')
    
#     return render(request, 'modalNovoAluno.html', {'form':form})

def salvarAluno(request):
    user = request.user
    cursoId = 1
    creditoId=1
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