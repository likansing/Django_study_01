from tabnanny import verbose
from django.db import models

# Create your models here.
class Campo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")#verbose name eh nome que aparece na tela para user

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao) #formata como aparecer na tela

class Atividade(models.Model):
    numero = models.IntegerField(verbose_name="Número")
    descricao = models.CharField(max_length=50, verbose_name="Descrição")
    pontos = models.DecimalField(decimal_places=1, max_digits=4)
    detalhes = models.CharField(max_length=100)
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT) #se deletar campo e existe uma chave estrangeria não deixa deletar

    def __str__(self):
        return "{} - {} ({})".format(self.numero, self.descricao, self.campo.nome)