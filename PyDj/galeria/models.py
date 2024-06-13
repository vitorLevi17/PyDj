from datetime import datetime

from django.db import models

class Fotografia(models.Model):

    opcoes_categoria = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALAXIA","Galaxia"),
        ("PLANETA","Planeta"),
    ]

    nome = models.CharField(max_length=50, null= False, blank= False)
    legenda = models.CharField(max_length=150, null= False, blank= False)
    categoria = models.CharField(max_length=50,choices=opcoes_categoria,default='')
    descricao = models.TextField(null= False, blank= False)
    foto = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    publicada = models.BooleanField(default = False)
    datas = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return f"Fotografia[nome = {self.nome}]"





