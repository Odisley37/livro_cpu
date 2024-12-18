# Generated by Django 5.1.4 on 2024-12-08 02:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unidade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Praca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_war', models.CharField(max_length=20)),
                ('graduacao', models.CharField(max_length=20)),
                ('numero', models.CharField(max_length=20)),
                ('matricula', models.IntegerField()),
                ('funcao', models.CharField(blank=True, max_length=100, null=True)),
                ('sangue', models.CharField(blank=True, max_length=2, null=True)),
                ('rh', models.CharField(blank=True, max_length=1, null=True)),
                ('data_nascimento', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pracas', to='unidade.unidade')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
