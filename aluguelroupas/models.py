from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    cep = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15, unique=True)

class Roupa(models.Model):
    nome = models.CharField(max_length=50)
    tamanho = models.CharField(max_length=15)
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    cor = models.CharField(max_length=25)
    tipo = models.CharField(max_length=15)
    descricao = models.TextField()
    situacao = models.CharField(max_length=50)
