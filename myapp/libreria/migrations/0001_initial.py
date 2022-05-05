# Generated by Django 4.0.4 on 2022-05-05 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='titulo')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='imagen')),
                ('descripcion', models.TextField(null=True, verbose_name='descripcion')),
            ],
        ),
    ]
