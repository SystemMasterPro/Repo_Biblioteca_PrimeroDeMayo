# Generated by Django 3.2.4 on 2021-06-26 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import registers.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('image', models.ImageField(upload_to=registers.models.url_book)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.IntegerField()),
                ('names', models.CharField(max_length=150)),
                ('surnames', models.CharField(max_length=150)),
                ('cycle', models.IntegerField()),
                ('image', models.ImageField(upload_to=registers.models.url_student)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Secretary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('deliver_date', models.DateField(verbose_name='Deliver Date')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registers.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registers.student')),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.IntegerField()),
                ('role', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registers.category'),
        ),
    ]