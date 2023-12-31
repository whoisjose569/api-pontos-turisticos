from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

class DocIdentificacao(models.Model):
    description = models.CharField(max_length=100)

class PontoTuristico(models.Model):
    nome = models.CharField('Nome', max_length=150)
    descricao = models.TextField('Descrição')
    aprovado = models.BooleanField('Aprovado', default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField('foto', upload_to='pontos_turisticos', null=True, blank=True)
    doc_identificacao = models.OneToOneField(DocIdentificacao, on_delete=models.CASCADE, null=True, blank=True)
    
    
    class Meta:
        verbose_name = "Ponto Turistico"
        verbose_name_plural = "Pontos Turisticos"
    
    @property
    def descricao_completa2(self):
        return '%s - %s' % (self.nome, self.endereco)
    
    def __str__(self):
        return self.nome
    
