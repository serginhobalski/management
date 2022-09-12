from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from employees.models import Employee


@login_required
def usuarios(request):
    usuarios = Employee.objects.all().order_by('-id')
    return render(request, 'employees/index.html', context={
        'usuarios': usuarios,
    })
