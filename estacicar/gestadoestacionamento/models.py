from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, )
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=10)


class Marca(models.Model):
    nome = models.CharField(max_length=50)


class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    placa =  models.CharField(max_length=7)
    cor =  models.CharField(max_length=5)
    observacoes =models.TextField()

