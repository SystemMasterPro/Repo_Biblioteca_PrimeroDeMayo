# Generated by Django 3.2.4 on 2021-09-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0014_auto_20210917_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deliver_date',
            field=models.DateField(verbose_name='Fecha de Entrega'),
        ),
    ]
