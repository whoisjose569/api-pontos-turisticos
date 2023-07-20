from django.db import models

class Atracao(models.Model):
    nome = models.CharField('Nome', max_length=150)
    descricao = models.TextField('Descriçao')
    horario_func = models.TextField('Horario Funcionamento')
    idade_minima = models.IntegerField('Idade Minima')
    foto = models.ImageField('foto', upload_to='atracoes', null=True, blank=True)
    
    class Meta:
        verbose_name = "Atração"
        verbose_name_plural = "Atrações"
        
    def __str__(self):
        return self.nome
    
