from django.db import models
from employees.models import Employee


# Create your models here.
class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.motivo
