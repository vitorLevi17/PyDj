from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

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
    publicada = models.BooleanField(default = True)
    datas = models.DateTimeField(default=datetime.now)
    usu = models.ForeignKey(
        to=User,
        on_delete =models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )

    def __str__(self):
        return self.nome





