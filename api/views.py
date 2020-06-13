from django.shortcuts import render
from rest_framework import viewsets

from .serializers import BoilerPlateCodeSerializer
from .models import BoilerPlateCode


class BoilerPlateCodeViewSet(viewsets.ModelViewSet):
    queryset = BoilerPlateCode.objects.all().order_by('language')
    serializer_class = BoilerPlateCodeSerializer
