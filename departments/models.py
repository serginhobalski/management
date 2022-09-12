from django.db import models


# Create your models here.
class Department(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome
