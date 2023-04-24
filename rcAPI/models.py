from django.db import models

# Create your models here.
class Inmueble(models.Model):
    #created = models.DateTimeField(auto_now_add=True)
    website = models.CharField(max_length=50)
    link = models.CharField(max_length=500)
    price_crawled = models.CharField(max_length=50)
    price_DOP = models.FloatField()
    title = models.CharField(max_length=200)
    rooms = models.IntegerField()
    bathrooms = models.FloatField()
    location_crawled  = models.CharField(max_length=200)
    sector  = models.CharField(max_length=200)
    province  = models.CharField(max_length=200)
    condition  = models.CharField(max_length=200)
    current_use  = models.CharField(max_length=200)
    square_footage = models.IntegerField()
    floor = models.SmallIntegerField()
    elevator = models.SmallIntegerField()
    buildable = models.BooleanField()
    construction_year = models.CharField(max_length=30)
    amenities = models.TextField()
    amount_amenities = models.SmallIntegerField()
    image_link = models.CharField(max_length=500)
    banos = models.BooleanField()
    aguaPotable = models.BooleanField()
    aireAcondicionado = models.BooleanField()
    areaJuego = models.BooleanField()
    areaServicio = models.BooleanField()
    ascensor = models.BooleanField()
    balcon = models.BooleanField()
    cisterna = models.BooleanField()
    controlAcceso = models.BooleanField()
    cuartoServicio = models.BooleanField()
    estarFamiliar = models.BooleanField()
    estudio = models.BooleanField()
    gazebo = models.BooleanField()
    gimnasio = models.BooleanField()
    inversor = models.BooleanField()
    jacuzzi = models.BooleanField()
    lobby = models.BooleanField()
    patio = models.BooleanField()
    picuzzi = models.BooleanField()
    piscina = models.BooleanField()
    plantaElectrica = models.BooleanField()
    pozo = models.BooleanField()
    satelite = models.BooleanField()
    sauna = models.BooleanField()
    seguridad = models.BooleanField()
    shutters = models.BooleanField()
    terraza = models.BooleanField()
    vestidores = models.BooleanField()

class Prediction(models.Model):
    rooms = models.FloatField()
    bathrooms = models.FloatField()
    squarefootage = models.FloatField()
    province = models.IntegerField()
    banos = models.BooleanField()
    aguaPotable = models.BooleanField()
    aireAcondicionado = models.BooleanField()
    areaJuegosInfantiles = models.BooleanField()
    areaServicio = models.BooleanField()
    ascensor = models.BooleanField()
    balcon = models.BooleanField()
    cisterna = models.BooleanField()
    controlAcceso = models.BooleanField()
    cuartoServicio = models.BooleanField()
    estarFamiliar = models.BooleanField()
    estudio = models.BooleanField()
    gazebo = models.BooleanField()
    gimnasio = models.BooleanField()
    inversor = models.BooleanField()
    jacuzzi = models.BooleanField()
    lobby = models.BooleanField()
    patio = models.BooleanField()
    picuzzi = models.BooleanField()
    piscina = models.BooleanField()
    plantaElectrica = models.BooleanField()
    pozo = models.BooleanField()
    satelite = models.BooleanField()
    sauna = models.BooleanField()
    seguridad = models.BooleanField()
    shutters = models.BooleanField()
    terraza = models.BooleanField()
    vestidores = models.BooleanField()

    def __str__(self):
        return self.squarefootage