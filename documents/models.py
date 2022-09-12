from django.db import models
from employees.models import Employee


# Create your models here.
class Document(models.Model):
    descricao = models.CharField(max_length=100)
    owner = models.ForeignKey(
        Employee, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.descricao
