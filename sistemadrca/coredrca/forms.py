from django import forms
from .models import Aluno

class BuscaAlunoForm(forms.ModelForm):
    busca = forms.CharField(required=True, widget=forms.TextInput(attrs={'name' : 'busca'}))

    class Meta:
        model = Aluno
        fields = ['busca']

class AlunoForm(forms.ModelForm):
    nomeAtual = forms.CharField(required=True, widget=forms.TextInput(attrs={'name' : 'nomeAtual'}))
    matriculaAtual = forms.CharField(required=True, widget=forms.TextInput(attrs={'name' : 'matriculaAtual'}))

    class Meta:
        model = Aluno
        fields = ['nomeAtual', 'matriculaAtual']

    def clean(self):
        nomeAtual = self.cleaned_data.get('nomeAtual')
        matriculaAtual = self.cleaned_data.get('matriculaAtual')

        if nomeAtual is None or matriculaAtual is None:
            raise forms.ValidationError("O Nome e a Matrícula do aluno são obrigatórios")
        return self.cleaned_data