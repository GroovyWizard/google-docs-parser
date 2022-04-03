from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from htmlparser.serializers import *

class RawArchiveViewSet(viewsets.ModelViewSet):
    queryset = RawArchive.objects.all()
    serializer_class = RawArchiveSerializer