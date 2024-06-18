from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Fotografia


def index(request):
    fotos = Fotografia.objects.order_by("-datas").filter(publicada = True)
    return render(request, 'galeria/index.html',{"cards":fotos})


def imagem(request,id):
    fotografia = get_object_or_404(Fotografia, pk=id)
    return render(request, 'galeria/imagem.html',{"fotografia":fotografia})

def buscar(request):
    fotos = Fotografia.objects.order_by("-datas").filter(publicada=True)

    if "buscar" in request.GET:
        nome_busca = request.GET['buscar']
        if nome_busca:
            fotos = fotos.filter(nome__icontains=nome_busca)

    return render(request,'galeria/buscar.html',{"cards":fotos})