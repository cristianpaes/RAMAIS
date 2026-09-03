from django.db import models


class Setores(models.Model):
    setor = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Setor"
    )

    class Meta:
        db_table = "setores"
        verbose_name = "Setor"
        verbose_name_plural = "Setores"
        ordering = ["setor"]

    def __str__(self):
        return self.setor


class Empresas(models.Model):
    nome_emp = models.CharField(
        max_length=250,
        verbose_name="Empresa"
    )

    cnpj = models.CharField(
        max_length=21,
        verbose_name="CNPJ"
    )

    insc_estadual = models.CharField(
        max_length=13,
        blank=True,
        verbose_name="Inscrição Estadual"
    )

    telefone_emp = models.CharField(
        max_length=13,
        verbose_name="Telefone"
    )

    rua = models.CharField(
        max_length=500,
        verbose_name="Endereço"
    )

    numero = models.CharField(
        max_length=6,
        verbose_name="Número"
    )

    complemento = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Complemento"
    )

    bairro = models.CharField(
        max_length=150,
        verbose_name="Bairro"
    )

    cep = models.CharField(
        max_length=9,
        verbose_name="CEP"
    )

    class Meta:
        db_table = "empresas"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ["nome_emp"]

    def __str__(self):
        return self.nome_emp


class Ramais(models.Model):
    ramal = models.CharField(
        max_length=4,
        verbose_name="Ramal"
    )

    nome_resp = models.CharField(
        max_length=30,
        verbose_name="Responsável"
    )

    email = models.EmailField(
        max_length=60,
        verbose_name="Email"
    )

    setor_ramais = models.ForeignKey(
        Setores,
        on_delete=models.DO_NOTHING,
        verbose_name="Setor"
    )

    empresa_ramais = models.ForeignKey(
        Empresas,
        on_delete=models.DO_NOTHING,
        verbose_name="Empresa"
    )

    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de criação"
    )

    class Meta:
        db_table = "ramais"
        verbose_name = "Ramal"
        verbose_name_plural = "Ramais"
        ordering = ["ramal"]

    def __str__(self):
        return (
            f"{self.ramal} - "
            f"{self.nome_resp} - "
            f"{self.setor_ramais} - "
            f"{self.empresa_ramais}"
        )

    def get_data_criacao(self):
        return self.data_criacao.strftime("%d/%m/%Y")