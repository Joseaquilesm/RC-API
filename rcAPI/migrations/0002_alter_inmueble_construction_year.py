# Generated by Django 4.2 on 2023-04-21 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rcAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='construction_year',
            field=models.CharField(max_length=30),
        ),
    ]
