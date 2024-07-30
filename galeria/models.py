from django.db import models
from datetime import datetime

class Fotografia(models.Model):

    opcoes_categoria = [
        ('Nebulosa', 'Nebulosa'),
        ('Estrela', 'Estrela'),
        ('Galáxia', 'galáxia'),
        ('Planeta', 'Planeta'),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=200, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=opcoes_categoria, default='')
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

