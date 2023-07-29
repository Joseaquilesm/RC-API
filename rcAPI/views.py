from django.shortcuts import render
from .models import Inmueble, Prediction, User
from rest_framework import viewsets, permissions
from .serializers import InmuebleSerializer
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import pickle as pkl
import numpy as np
import json
import jwt, datetime
import pandas as pd




class InmuebleViewSet(viewsets.ModelViewSet):
    queryset = Inmueble.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InmuebleSerializer

@api_view(["GET"])
def getUsers(request):
    token = request.COOKIES.get('jwt')

    if not token:
        raise AuthenticationFailed('Unauthorized')
    
    try:
        payload = jwt.decode(token, 'secret', algorithms =['HS256']) 
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthorized')
    
    user = User.objects.filter(id = payload['id']).first()
    serializer = UserSerializer(user)

    return Response(serializer.data)


@api_view(["POST"])
def login(request):
    email = request.data['email']
    password = request.data['password']

    user = User.objects.filter(email = email).first()
    if user is None:
        raise AuthenticationFailed('User not found!')
    
    if not user.check_password(password):
        raise AuthenticationFailed('Incorrect password')
    
    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 60),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret', algorithm ='HS256')

    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }

    return response

@api_view(["POST"])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = { 
        'message': 'success'
    }
    return response


@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def predict(request):
    try:
        mydata = request.data
        unit = np.array(list(mydata.values()))
        
        bedrooms = unit[0]
        beds = unit[1]
        baths = unit[2]
        province = unit[3]
        place_type = unit[4]
        place_description = unit[5]
        print(unit)
        if(len(unit) == 6):
            print("you sent an empty array")
            tv = 0
            washer = 0
            free_parking = 0
            dedicated_workspace = 0
            piscina = 0
            fire_pit = 0
            lake_access = 0
            beach_access = 0
        else:
         array = rebuildArray(unit)
         tv = array[0]
         washer = array[1]
         free_parking = array[2]
         dedicated_workspace = array[3]
         piscina = array[4]
         fire_pit = array[5]
         lake_access = array[6]
         beach_access = array[7]
        print("THIS IS WHAT YOU WANT TO SEE")
        print(place_type)
        print(place_description)
        print(get_place_type_id("hotel"))
        resultado = get_price_prediction(bedrooms,beds,baths,province,place_description,
                      place_type,tv,washer,
                      free_parking,dedicated_workspace,piscina,fire_pit,lake_access,
                      beach_access)
        print(resultado)
        return JsonResponse(resultado, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def rebuildArray(data):
    dictionaries = []
    arr = []
    for item in data:
         if isinstance(item, dict):
            dictionaries.append(item)

    for item in dictionaries:
        if item == 'Tv':
            print("tv")


    newArr = []
    tv_flag = False
    washer_flag = False
    freeparking_flag = False
    dedicatedworkspace_flag = False
    pool_flag = False
    firepit_flag = False
    lakeaccess_flag = False
    beachaccess_flag = False
    for element_dict in dictionaries:
        if  element_dict.get("name") == "Tv" :
            print("what tv prints on true " + str(element_dict))
            newArr.append(1) 
            tv_flag=True 
            continue
        else:
            if tv_flag == False:
             print("what tv prints on false " + str(element_dict))
             newArr.append(0)

        if element_dict.get("name") == "Washer" :
            newArr.append(1)
            washer_flag=True
            print("what washer prints on true " + str(element_dict))
            continue
        else:
            if washer_flag == False:
                print("what washer prints on false " + str(element_dict))
                newArr.append(0)

        if element_dict.get("name") == "Free parking" :
            print("what free parking prints on true " + str(element_dict))
            newArr.append(1)
            freeparking_flag=True
            continue
        else:
            if freeparking_flag == False:
                print("what free parking prints on false " + str(element_dict))
                newArr.append(0)

        if element_dict.get("name") == "dedicated workspace" :
            print("what dedicated workspace prints on true " + str(element_dict))
            newArr.append(1)
            dedicatedworkspace_flag=True
            continue
        else:
            if dedicatedworkspace_flag == False:
                print("what dedicated workspace prints on false " + str(element_dict))
                newArr.append(0)

        if element_dict.get("name") == "pool" :
            print("what pool prints on true " + str(element_dict))
            newArr.append(1)
            pool_flag=True
            continue
        else:
            if pool_flag == False:
                print("what pool prints on false " + str(element_dict))
                newArr.append(0)

        if element_dict.get("name") == "fire pit" :
            print("what fire pit prints on true " + str(element_dict))
            newArr.append(1)
            firepit_flag=True
            continue
        else:
            if firepit_flag == False:
                print("what fire pit prints on false " + str(element_dict))
                newArr.append(0)

        if element_dict.get("name") == "lake access" :
            print("what lake access prints on true " + str(element_dict))
            newArr.append(1)
            lakeaccess_flag=True
            continue
        else:
            if lakeaccess_flag == False:
                print("what lake access prints on FALSE " + str(element_dict))
                newArr.append(0)

        if element_dict.get("name") == "beach access" :
            print("what beach access prints on true " + str(element_dict))
            newArr.append(1)
            beachaccess_flag=True
            continue
        else:
            if beachaccess_flag == False:
                print("what beach access prints on false " + str(element_dict))
                newArr.append(0)
        
    while len(newArr) < 8:
        newArr.append(0)
        
    print(newArr)
    return newArr



def get_price_prediction(bedrooms, beds, baths, province, place_type, 
                         place_description, tv, washer, free_parking, 
                         dedicated_workspace, piscina, fire_pit, 
                         lake_access, beach_access):
    # Load the trained model from the pickle file
    with open('rcAPI\model\Random_Forest_Regressor_model.pickle', 'rb') as file:
        model = pkl.load(file)

    # Sample new data for prediction
    new_data = pd.DataFrame({
        'guests': [1],
        'bedrooms': [bedrooms],
        'beds': [beds],
        'baths': [baths],
        'province': [get_province_id(province)],
        'amount_nights': [4],
        'place_type': [get_place_type_id(place_type)],
        'place_description': [get_place_desc_id(place_description)],
        'tv': [tv],
        'washer': [washer],
        'free_parking': [free_parking],
        'dedicated_workspace': [dedicated_workspace],
        'pool': [piscina],
        'fire_pit': [fire_pit],
        'lake_access': [lake_access],
        'beach_access': [beach_access]
    })
    print(new_data.to_string())
    # Convert categorical variables into numerical data using one-hot encoding
    #new_data = pd.get_dummies(new_data, columns=['province', 'place_type', 'place_description'], drop_first=True)

    # Make predictions using the loaded model
    predicted_prices = model.predict(new_data)
    _price = predicted_prices[0]
    # Print the predicted prices
    #print(_price)

    #=============== CONVERTING TO PESOS DOMINICANOS
    converted_price = (_price * 4) * 56.30
    return converted_price

def get_province_id(name):
    if(name == "Elias Pina"):
        return 1
    if(name == "Bahoruco"):
        return 2
    if(name == "Independencia"):
        return 3
    if(name == "Sanchez Ramirez"):
        return 4
    if(name == "San Juan"):
        return 5
    if(name == "Santiago Rodriguez"):
        return 6
    if(name == "Valverde"):
        return 7
    if(name == "Hato Mayor"):
        return 8
    if(name == "Pedernales"):
        return 9
    if(name == "El Seibo"):
        return 10
    if(name == "Monte Cristi"):
        return 11
    if(name == "Barahona"):
        return 12
    if(name == "Monsenor Nouel"):
        return 13
    if(name == "Monte Plata"):
        return 14
    if(name == "Hermanas Mirabal"):
        return 15
    if(name == "San Jose de Ocoa"):
        return 16
    if(name == "Peravia"):
        return 17
    if(name == "Azua"):
        return 18
    if(name == "Dajabon"):
        return 19
    if(name == "Duarte"):
        return 20
    if(name == "Espaillat"):
        return 21
    if(name == "Maria Trinidad Sanchez"):
        return 22
    if(name == "San Cristobal"):
        return 23
    if(name == "La Romana"):
        return 24
    if(name == "San Pedro de Macoris"):
        return 25
    if(name == "La Vega"):
        return 26
    if(name == "Puerto Plata"):
        return 27
    if(name == "Santiago"):
        return 28
    if(name == "La Altagracia"):
        return 29
    if(name == "Samana"):
        return 30
    if(name == "Santo Domingo"):
        return 31
    
def get_place_type_id(name):
    if(name == "Entire place"):
        return 3
    if(name == "Partial"):
        return 2
    if(name == "Shared"):
        return 1


def get_place_desc_id(name):
    if(name == "Casa"):
        return 6
    if(name == "Apartamento" or name == "Apartment"):
        return 5
    if(name == "Hotel"):
        return 4
    if(name == "Cabanas"):
        return 3
    if(name == "Granja"):
        return 2
    if(name == "Domo"):
        return 1


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
