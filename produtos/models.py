from django.db import models

class Pessoa(models.Model):
    nome = models.TextField(null=True)
    idade = models.IntegerField()

    def __str__(self) -> str:
        return self.nome