from django.db import models

class Clientes(models.Model):
    id_clientes = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=50)
    identificacao = models.CharField(max_length=50)
    classificacao = models.CharField(max_length=18)
    tipo_pessoa = models.CharField(max_length=10)
    cnpj_cpf = models.CharField(max_length=15)
    inscricao_estadual = models.CharField(max_length=20)
    inscricao_municipal = models.CharField(max_length=20)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    nome_titular = models.CharField(max_length=50)
    cpf = models.CharField(max_length=15)
    funcao = models.CharField(max_length=50)

class Empresas(models.Model):
    id_empresas = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=50)
    tipo_pessoa = models.CharField(max_length=10)
    cnpj = models.CharField(max_length=15)
    inscricao_estadual = models.CharField(max_length=20)
    inscricao_municipal = models.CharField(max_length=20)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    nome_titular = models.CharField(max_length=50)
    cpf = models.CharField(max_length=15)
    funcao = models.CharField(max_length=50)

class LancamentosReceber(models.Model):
    id_lancamentos_receber = models.AutoField(primary_key=True)
    clientes_id_clientes = models.ForeignKey('Clientes', on_delete=models.CASCADE)
    empresas_id_Empresas = models.ForeignKey('Empresas', on_delete=models.CASCADE)
    data_vencimento = models.CharField(max_length=12)
    data_emissao = models.CharField(max_length=12)
    valor_titulo = models.CharField(max_length=14)
    numero_documento = models.CharField(max_length=20)




