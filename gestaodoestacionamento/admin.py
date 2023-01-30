from django.contrib import admin
from .models import Pessoa, Veiculo, Marca

admin.site.register(Pessoa)
admin.site.register(Veiculo)
admin.site.register(Marca)

