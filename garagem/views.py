from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from garagem.models import Marca
from garagem.serializers import MarcaSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer