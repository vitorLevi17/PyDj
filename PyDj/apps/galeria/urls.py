from django.urls import path
from apps.galeria.views import *


urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:id>',imagem, name='imagem'),
    path('buscar',buscar, name='buscar'),
    path('nova-imagem',nova_imagem, name='nova_imagem'),
    path('editar-imagem/<int:id>', editar_imagem, name='editar_imagem'),
    path('excluir-imagem/<int:id>',excluir_imagem, name='excluir_imagem'),
    path('filtro/<str:categoria>',filtro,name = 'filtro')

]
