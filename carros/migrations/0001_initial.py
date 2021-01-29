# Generated by Django 2.2 on 2020-12-04 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=100)),
                ('ano', models.DateField()),
                ('cor', models.CharField(max_length=100)),
                ('placa', models.CharField(max_length=50)),
            ],
        ),
    ]