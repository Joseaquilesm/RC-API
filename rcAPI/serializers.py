from rest_framework import serializers
from .models import Inmueble
from .models import Prediction
from .models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class InmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmueble
        fields = ('id',
                  'website',
                  'link',
                  'price_crawled',
                  'price_DOP',
                  'title',
                  'rooms',
                  'bathrooms',
                  'location_crawled',
                  'sector',
                  'province',
                  'condition',
                  'current_use',
                  'square_footage',
                  'floor',
                  'elevator',
                  'buildable',
                  'construction_year',
                  'amenities',
                  'amount_amenities',
                  'image_link',
                  'banos',
                  'aguaPotable',
                  'aireAcondicionado',
                  'areaJuego',
                  'areaServicio',
                  'ascensor',
                  'balcon',
                  'cisterna',
                  'controlAcceso',
                  'cuartoServicio',
                  'estarFamiliar',
                  'estudio',
                  'gazebo',
                  'gimnasio',
                  'inversor',
                  'jacuzzi',
                  'lobby',
                  'patio',
                  'picuzzi',
                  'piscina',
                  'plantaElectrica',
                  'pozo',
                  'satelite',
                  'sauna',
                  'seguridad',
                  'shutters',
                  'terraza',
                  'vestidores')
                
class predictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = '__all__'
