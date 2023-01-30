from django.db import models
import math

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=200)
    Telefone = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    

class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete= models.CASCADE)
    placa = models.CharField(max_length=6)
    proprietario = models.ForeignKey(Pessoa, on_delete= models.CASCADE)
    cor = models.CharField(max_length=6)
    observacao = models.TextField()

    def __str__(self):
        return self.marca.nome + ' - ' + self.placa

class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=6, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "Preficicação do serviço"

class ClienteRotativo(models.Model):    
    entrada= models.DateTimeField(auto_now=False)
    saida = models.DateTimeField(auto_now=False, null=True, blank=True)
    valor_hora= models.DecimalField(max_digits=6, decimal_places=2)
    veiculo= models.ForeignKey(Veiculo, on_delete= models.CASCADE)
    pago = models.BooleanField(default=False)


    def tempo_decorrido(self):        
        return math.ceil ((self.entrada-self.saida).total_seconds()/3600)

    def horas(self):
        self.valor_hora * self.tempo_decorrido 

    def __str__(self):
        return self.veiculo.placa





