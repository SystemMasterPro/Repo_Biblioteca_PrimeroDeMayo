# Generated by Django 3.2.4 on 2021-09-17 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0008_auto_20210917_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalusers',
            name='phone',
            field=models.CharField(blank=True, db_index=True, max_length=9, null=True, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(blank=True, max_length=9, null=True, unique=True, verbose_name='Telefono'),
        ),
    ]
