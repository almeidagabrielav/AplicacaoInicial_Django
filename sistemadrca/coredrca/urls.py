from django.urls import path
from coredrca import views

urlpatterns = [
    path(r'^artigo/(?P<ano>[0-9]{4})/$', views.artigo, name='artigo'),
]
