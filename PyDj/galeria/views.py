from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    dados = {
        1: {"Nome": "Nebulosa de Carina",
            "legenda": "webbtelecospe.org / NASA / James Web"},
        2: {"Nome": "Karina de Nebulosa",
            "legenda": "ellonMusk.org / NASA / Rodriguez  Web"}
    }
    return render(request, 'galeria/index.html',{"cards":dados})


def imagem(request):
    return render(request, 'galeria/imagem.html')
