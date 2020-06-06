from django.db import models


# Create your models here.

class Setores(models.Model):
    setor = models.CharField(max_length=150, unique=True)

    class Meta:
        db_table = 'setores'

    def __str__(self):
        return self.setor

class Empresas(models.Model):
    nome_emp = models.CharField(max_length=250,verbose_name='Empresa')
    cnpj = models.CharField(max_length=21, verbose_name='CNPJ')
    insc_estadual= models.CharField(max_length=13, blank=True, verbose_name='Inscrição Estadual')
    telefone_emp = models.CharField(max_length=13, verbose_name='Telefone')
    rua = models.CharField(max_length=500, verbose_name='Endereço')
    numero = models.CharField(max_length=6, verbose_name='Número')
    complemento = models.CharField(max_length=150, blank=True, verbose_name='Complemento')
    bairro = models.CharField(max_length=150, verbose_name='Bairro')
    cep = models.CharField(max_length=9, verbose_name='CEP')

    class Meta:
        db_table = 'empresas'

    def __str__(self):
        return self.nome_emp


class Ramais(models.Model):
    ramal = models.CharField(max_length=4, verbose_name='Ramal')
    nome_resp = models.CharField(max_length=30, verbose_name='Responsavél')
    email = models.EmailField(max_length=60)
    setor_ramais = models.ForeignKey(Setores, on_delete= models.DO_NOTHING, verbose_name='Setor')
    empresa_ramais = models.ForeignKey(Empresas,on_delete= models.DO_NOTHING, verbose_name='Empresa')
    data_criacao = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'ramais'

    def __str__(self):
        return self.ramal + str(self.setor_ramais)+ str(self.empresa_ramais)

    def get_data_criacao(self):
        return self.data_criacao.strftime('%d/%m/%Y')

