# Generated by Django 3.2.4 on 2021-09-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0015_alter_order_deliver_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deliver_date',
            field=models.DateTimeField(verbose_name='Fecha de Entrega'),
        ),
    ]