from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Fotografia


def index(request):
    fotos = Fotografia.objects.all()
    return render(request, 'galeria/index.html',{"cards":fotos})


def imagem(request,id):
    fotografia = get_object_or_404(Fotografia, pk=id)
    return render(request, 'galeria/imagem.html',{"fotografia":fotografia})
