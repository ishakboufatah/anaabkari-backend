from django.shortcuts import render

#from httplib2 import Authentication

from urllib import request
from .models import Clase, SubjectsPrimary1,SubjectsPrimary2,USER
from .serializers import ClaseSerializer,SubjectsPrimary1Serializer,SubjectsPrimary2Serializer,USERSerializer
import anaabkari.urls  

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class ClaseViewSet(viewsets.ModelViewSet):
    permission_classes =[DjangoModelPermissions]
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

class SubjectsPrimary1ViewSet(viewsets.ModelViewSet):
    permission_classes =[DjangoModelPermissions]
    queryset = SubjectsPrimary1.objects.all()
    serializer_class = SubjectsPrimary1Serializer

class SubjectsPrimary2ViewSet(viewsets.ModelViewSet):
    permission_classes =[DjangoModelPermissions]
    queryset = SubjectsPrimary2.objects.all()
    serializer_class = SubjectsPrimary2Serializer

class USERViewSet(viewsets.ModelViewSet):
    permission_classes =[DjangoModelPermissions]
    queryset = USER.objects.all()
    serializer_class = USERSerializer
