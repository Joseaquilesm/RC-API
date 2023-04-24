from rest_framework import routers
from . import views
from django.urls import path, include


router = routers.DefaultRouter()

#router.register('api/inmueble', views.InmuebleViewSet, 'inmueble')
#router.register('api/predict', views.predict, 'prediction')
#urlpatterns = router.urls
router.register('rcAPI', views.InmuebleViewSet)
urlpatterns = [
    path('api/',include(router.urls)),
    path('predict/',views.predict),
]