# Generated by Django 4.2 on 2023-04-21 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcAPI', '0003_remove_inmueble_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inmueble',
            old_name='location',
            new_name='location_crawled',
        ),
    ]
