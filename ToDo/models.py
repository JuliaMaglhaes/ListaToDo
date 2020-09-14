from django.db import models

class Lista (models.Model):
    titulo = models.CharField(max_length=200)
    check = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Lista'
        verbose_name_plural = 'Listas'
        ordering = ['-criado']
    
