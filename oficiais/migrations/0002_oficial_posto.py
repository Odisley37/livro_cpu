# Generated by Django 5.1.4 on 2024-12-08 02:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficiais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oficial',
            name='posto',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
    ]