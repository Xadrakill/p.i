# Generated by Django 5.1.1 on 2024-12-05 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_pais_tipoviagem_pacoteviagem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PacoteViagem',
        ),
    ]
