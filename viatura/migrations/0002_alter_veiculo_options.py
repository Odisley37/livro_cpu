# Generated by Django 5.1.4 on 2024-12-08 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viatura', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='veiculo',
            options={'ordering': ['prefixo']},
        ),
    ]