# Generated by Django 5.0 on 2024-01-30 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Marca',
        ),
    ]