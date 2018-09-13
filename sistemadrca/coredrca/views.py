from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader
from django.template.loader import render_to_string

# Create your views here.

def artigo(request, ano):
    return HttpResponse("Olá Mundo, estamos no ano " + ano)

def home(request):
    #template = loader.get_template("index.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))