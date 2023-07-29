from rest_framework import routers
from . import views
from django.urls import path, include


router = routers.DefaultRouter()

#router.register('api/inmueble', views.InmuebleViewSet, 'inmueble')
#router.register('api/predict', views.predict, 'prediction')
#urlpatterns = router.urls
router.register('inmuebles', views.InmuebleViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('api/predict',views.predict),
    path('api/register', views.register),
    path('api/login', views.login),
    path('api/user', views.getUsers),
    path('api/logout', views.logout)
]