from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Solicitante
from django.http import JsonResponse
# Create your views here.

class SolicitudesListView(View):
    def get(self, request):
        sList = Solicitante.objects.all()
        return JsonResponse(list(sList.values()), safe=False)

class SolicitudesDetailView(View):
    def get(self, request, pk):
        list= Solicitante.objects.get(pk=pk)
        return JsonResponse(list, safe=False)