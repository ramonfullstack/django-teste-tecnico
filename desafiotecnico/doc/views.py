from django.shortcuts import render

from rest_framework import viewsets
from .models import Doc
from .serializers import DocSerializer

class DocViewSet(viewsets.ModelViewSet):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer
