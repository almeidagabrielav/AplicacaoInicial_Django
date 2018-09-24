from django import forms
from .models import Aluno

class ProductForm(form.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'matricula', 'curso', 'credito', 'disciplinas']