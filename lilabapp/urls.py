from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import SolicitudesListView
urlpatterns = [
    path('solicitudes/', SolicitudesListView.as_view(), name='solicitudes_list')
    
    ] 