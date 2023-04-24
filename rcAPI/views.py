from django.shortcuts import render
from .models import Inmueble, Prediction
from rest_framework import viewsets, permissions
from .serializers import InmuebleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import pickle as pkl
import numpy as np
import json



#it would probably be a good idea to move this to the views.py
class InmuebleViewSet(viewsets.ModelViewSet):
    queryset = Inmueble.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InmuebleSerializer


@api_view(["POST"])
def predict(request):
    try:
        mydata = request.data
        unit = np.array(list(mydata.values()))
        rooms = unit[0]
        bathrooms = unit[1]
        squarefootage = unit[2]
        province = unit[3]
        banos = unit[4]
        aguaPotable = unit[5]
        aireAcondicionado = unit[6]
        areaJuegosInfantiles = unit[7]
        areaServicio = unit[8]
        ascensor = unit[9]
        balcon = unit[10]
        cisterna = unit[11]
        controlAcceso = unit[12]
        cuartoServicio = unit[13]
        estarFamiliar = unit[14]
        estudio = unit[15]
        gazebo = unit[16]
        gimnasio = unit[17]
        inversor = unit[18]
        jacuzzi = unit[19]
        lobby = unit[20]
        patio = unit[21]
        picuzzi = unit[22]
        piscina = unit[23]
        plantaElectrica = unit[24]
        pozo = unit[25]
        satelite = unit[26]
        sauna = unit[27]
        seguridad = unit[28]
        shutters = unit[29]
        terraza = unit[30]
        vestidores = unit[31]
        
        resultado = predict_my_rental(rooms,bathrooms,squarefootage,province,banos,
                      aguaPotable,aireAcondicionado,areaJuegosInfantiles,
                      areaServicio,ascensor,balcon,cisterna,controlAcceso,
                      cuartoServicio,estarFamiliar,estudio,gazebo,gimnasio,
                      inversor,jacuzzi,lobby,patio,picuzzi,piscina,plantaElectrica,
                      pozo,satelite,sauna,seguridad,shutters,terraza,vestidores)
        print(resultado)
        return JsonResponse(resultado, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def predict_my_rental(rooms,bathrooms,squarefootage,province,banos,
                      aguaPotable,aireAcondicionado,areaJuegosInfantiles,
                      areaServicio,ascensor,balcon,cisterna,controlAcceso,
                      cuartoServicio,estarFamiliar,estudio,gazebo,gimnasio,
                      inversor,jacuzzi,lobby,patio,picuzzi,piscina,plantaElectrica,
                      pozo,satelite,sauna,seguridad,shutters,terraza,vestidores):
    
   
    lr_pickle = pkl.load(open("rcAPI\model\LR_model.pickle", 'rb'))
    _input = np.array([[rooms,bathrooms,squarefootage,province,banos,
                        aguaPotable,aireAcondicionado,areaJuegosInfantiles,
                        areaServicio,ascensor,balcon,cisterna,controlAcceso,
                        cuartoServicio,estarFamiliar,estudio,gazebo,gimnasio,
                        inversor,jacuzzi,lobby,patio,picuzzi,piscina,plantaElectrica,
                        pozo,satelite,sauna,seguridad,shutters,terraza,vestidores]])
    
    return lr_pickle.predict(_input)[0]

"""
@api_view(["POST"])
def predict(request):
    return Response()
        
def predict_my_rental(rooms,bathrooms,squarefootage,province,banos,
                      aguaPotable,aireAcondicionado,areaJuegosInfantiles,
                      areaServicio,ascensor,balcon,cisterna,controlAcceso,
                      cuartoServicio,estarFamiliar,estudio,gazebo,gimnasio,
                      inversor,jacuzzi,lobby,patio,picuzzi,piscina,plantaElectrica,
                      pozo,satelite,sauna,seguridad,shutters,terraza,vestidores):
    
    filenm = 'LR_model.pickle'
    lr_pickle = pkl.load(open(filenm, 'rb'))
    _input = np.array([[rooms,bathrooms,squarefootage,province,banos,
                        aguaPotable,aireAcondicionado,areaJuegosInfantiles,
                        areaServicio,ascensor,balcon,cisterna,controlAcceso,
                        cuartoServicio,estarFamiliar,estudio,gazebo,gimnasio,
                        inversor,jacuzzi,lobby,patio,picuzzi,piscina,plantaElectrica,
                        pozo,satelite,sauna,seguridad,shutters,terraza,vestidores]])
    return lr_pickle.predict(_input)[0]

"""

# Create your views here.
