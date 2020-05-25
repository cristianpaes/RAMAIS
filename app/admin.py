from django.contrib import admin
from app.models import Ramais, Empresas, Setores


# Register your models here.

@admin.register(Ramais)
class RamaisAdmin(admin.ModelAdmin):
    list_display = ['id','ramal','nome_resp', 'setor_ramais', 'email','empresa_ramais']
    list_per_page = 5

@admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = ['nome_emp']

@admin.register(Setores)
class SetoresAdmin(admin.ModelAdmin):
    list_display = ['setor']

