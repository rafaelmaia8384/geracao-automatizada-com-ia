# Introdução aos conceitos e aplicações do Django, um framework de alto nível em Python projetado para o desenvolvimento rápido de aplicações web seguras e sustentáveis.

from django.http import HttpResponse
from django.shortcuts import render

# Criando uma view para uma aplicação Django

def hello_world(request):
    # A requisição HTTP é passada como o primeiro argumento de cada view Django. O segundo argumento opcional é um dicionário de variáveis passadas à view.
    # Neste caso, estamos respondendo ao request com uma simples mensagem em HTML.
    return HttpResponse('Hello, World!')

# A 'url' para essa view é então declarada em urls.py:
# from django.urls import path
# from . import views
# urlpatterns = [path('', views.hello_world)]

# Com essas três simples partes, você pode desenvolver uma aplicação Django! Esta é uma introdução muito básica, mas Django é extremamente flexível e poderoso para desenvolvimento de aplicações web complexas.