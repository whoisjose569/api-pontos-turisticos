from django.db import models
from django.contrib.auth.models import User

class Avaliacao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField('Comentario', null=True, blank=True)
    nota = models.DecimalField('Nota', decimal_places=2, max_digits=3)
    data = models.DateTimeField('Data', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
    
    def __str__(self):
        return self.user.username
    
