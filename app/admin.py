from django.contrib import admin

from app.models import Empresas, Ramais, Setores


@admin.register(Ramais)
class RamaisAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "ramal",
        "nome_resp",
        "setor_ramais",
        "email",
        "empresa_ramais",
        "data_criacao",
    ]

    list_display_links = [
        "id",
        "ramal",
    ]

    list_filter = [
        "setor_ramais",
        "empresa_ramais",
        "data_criacao",
    ]

    search_fields = [
        "ramal",
        "nome_resp",
        "email",
        "setor_ramais__setor",
        "empresa_ramais__nome_emp",
    ]

    ordering = [
        "ramal",
    ]

    list_per_page = 10


@admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "nome_emp",
        "cnpj",
        "telefone_emp",
    ]

    search_fields = [
        "nome_emp",
        "cnpj",
        "telefone_emp",
    ]

    ordering = [
        "nome_emp",
    ]

    list_per_page = 10


@admin.register(Setores)
class SetoresAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "setor",
    ]

    search_fields = [
        "setor",
    ]

    ordering = [
        "setor",
    ]

    list_per_page = 10