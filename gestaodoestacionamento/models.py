from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=200)
    Telefone = models.CharField(max_length=200)
    

class Marca(models.Model):
    nome = models.CharField(max_length=50)

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete= models.CASCADE)
    placa = models.CharField(max_length=6)
    cor = models.CharField(max_length=6)
    observacao = models.TextField()





# Create your models here.
