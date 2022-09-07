from django.shortcuts import render
from django.contrib.auth.models import User
#from httplib2 import Authentication

from urllib import request
from .models import Clase, SubjectsPrimary1,SubjectsPrimary2,USER
from .serializers import ClaseSerializer,SubjectsPrimary1Serializer,SubjectsPrimary2Serializer,USERSerializer,UserSerializer
import anaabkari.urls  
from .permissions import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response


class ClaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner]
    # permission_classes =[DjangoModelPermissions]
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

class SubjectsPrimary1ViewSet(viewsets.ModelViewSet):
    # permission_classes =[DjangoModelPermissions]
    permission_classes = [IsOwner]
    # queryset = SubjectsPrimary1.objects.all()
    def get_queryset(self):
        
        user = self.request.user
        return SubjectsPrimary1.objects.filter(user=user)
    serializer_class = SubjectsPrimary1Serializer

class SubjectsPrimary2ViewSet(viewsets.ModelViewSet):
    # permission_classes =[DjangoModelPermissions]
    permission_classes = [IsOwner]
    # queryset = SubjectsPrimary2.objects.all()
    def get_queryset(self):
        
        user = self.request.user
        return SubjectsPrimary2.objects.filter(user=user)
    serializer_class = SubjectsPrimary2Serializer

class USERViewSet(viewsets.ModelViewSet):
    # permission_classes =[DjangoModelPermissions]
    permission_classes = [IsOwner]
    # queryset = USER.objects.all()
    def get_queryset(self):
        
        user = self.request.user
        return USER.objects.filter(user=user)
    serializer_class = USERSerializer

class UserViewSet(viewsets.ModelViewSet):
    # permission_classes =[DjangoModelPermissions]
    permission_classes = [IsOwner]
    # queryset = USER.objects.all()
    def get_queryset(self):
        
        user = self.request.user
        return User.objects.filter(username=user)
    serializer_class = UserSerializer
