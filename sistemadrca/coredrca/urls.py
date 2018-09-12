from django.urls import path, include, re_path
from coredrca import views

urlpatterns = [
    re_path(r'artigo/(?P<ano>[0-9]{4})/$', views.artigo, name='artigo'),
    path('', views.home, name='home'),
]
