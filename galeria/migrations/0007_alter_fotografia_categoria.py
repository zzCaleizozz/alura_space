# Generated by Django 5.0.7 on 2024-07-30 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0006_alter_fotografia_categoria_alter_fotografia_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('Nebulosa', 'Nebulosa'), ('Estrela', 'Estrela'), ('Galáxia', 'galáxia'), ('Planeta', 'Planeta')], default='', max_length=100),
        ),
    ]
