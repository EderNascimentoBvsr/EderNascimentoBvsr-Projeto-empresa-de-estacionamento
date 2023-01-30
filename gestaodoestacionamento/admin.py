from django.contrib import admin
from .models import Pessoa, Veiculo, Marca, Parametros, ClienteRotativo

admin.site.register(Pessoa)
admin.site.register(Veiculo)
admin.site.register(Marca)
admin.site.register(Parametros)
admin.site.register(ClienteRotativo)

