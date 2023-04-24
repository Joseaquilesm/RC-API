# Generated by Django 4.2 on 2023-04-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('website', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=500)),
                ('price_crawled', models.CharField(max_length=50)),
                ('price_DOP', models.FloatField()),
                ('title', models.CharField(max_length=200)),
                ('rooms', models.IntegerField()),
                ('bathrooms', models.FloatField()),
                ('location', models.CharField(max_length=200)),
                ('sector', models.CharField(max_length=200)),
                ('province', models.CharField(max_length=200)),
                ('condition', models.CharField(max_length=200)),
                ('current_use', models.CharField(max_length=200)),
                ('square_footage', models.IntegerField()),
                ('floor', models.SmallIntegerField()),
                ('elevator', models.SmallIntegerField()),
                ('buildable', models.BooleanField()),
                ('construction_year', models.SmallIntegerField()),
                ('amenities', models.TextField()),
                ('amount_amenities', models.SmallIntegerField()),
                ('image_link', models.CharField(max_length=500)),
                ('banos', models.BooleanField()),
                ('aguaPotable', models.BooleanField()),
                ('aireAcondicionado', models.BooleanField()),
                ('areaJuego', models.BooleanField()),
                ('areaServicio', models.BooleanField()),
                ('ascensor', models.BooleanField()),
                ('balcon', models.BooleanField()),
                ('cisterna', models.BooleanField()),
                ('controlAcceso', models.BooleanField()),
                ('cuartoServicio', models.BooleanField()),
                ('estarFamiliar', models.BooleanField()),
                ('estudio', models.BooleanField()),
                ('gazebo', models.BooleanField()),
                ('gimnasio', models.BooleanField()),
                ('inversor', models.BooleanField()),
                ('jacuzzi', models.BooleanField()),
                ('lobby', models.BooleanField()),
                ('patio', models.BooleanField()),
                ('picuzzi', models.BooleanField()),
                ('piscina', models.BooleanField()),
                ('plantaElectrica', models.BooleanField()),
                ('pozo', models.BooleanField()),
                ('satelite', models.BooleanField()),
                ('sauna', models.BooleanField()),
                ('seguridad', models.BooleanField()),
                ('shutters', models.BooleanField()),
                ('terraza', models.BooleanField()),
                ('vestidores', models.BooleanField()),
            ],
        ),
    ]