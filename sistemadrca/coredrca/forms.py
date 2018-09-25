from django import forms
from .models import Aluno

class ProductForm(form.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'matricula', 'curso', 'credito', 'disciplinas']

class AlunoForm(forms.Form):
    nomeAtual = forms.CharField(max_length=100)
    matriculaAtual = forms.CharField(max_length=50)