from django.contrib import admin
from .models import Marca, Categoria, Cor, Acessorio

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Acessorio)
admin.site.register(Cor)
