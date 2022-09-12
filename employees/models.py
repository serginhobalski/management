from companies.models import Company
from departments.models import Department
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Employee(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    department = models.ManyToManyField(Department)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.nome
