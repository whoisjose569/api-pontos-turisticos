from django.db import models

class Endereco(models.Model):
    linha1 = models.CharField('Linha1', max_length=150)
    linha2 = models.CharField('Linha2', max_length=150, null=True, blank=True)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=50)
    pais = models.CharField('País', max_length=70)
    latitude = models.IntegerField('Latitude', null=True, blank=True)
    longitude = models.IntegerField('Longitude', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
    
    def __str__(self):
        return self.linha1
    
