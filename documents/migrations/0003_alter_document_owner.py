# Generated by Django 4.1.1 on 2022-09-06 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_user'),
        ('documents', '0002_document_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='employees.employee'),
            preserve_default=False,
        ),
    ]