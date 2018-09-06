from django.shortcuts import render

# Create your views here.

def artigo(request, ano):
    return HttpResponse("Olá Mundo, estamos no ano " + ano)