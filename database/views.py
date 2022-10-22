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
    serializer_class = USERSerializer
    
    def get_queryset(self):
        queryset = USER.objects.all()
        user = self.request.user
        print(user)
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset
    

class UserViewSet(viewsets.ModelViewSet):
    # permission_classes =[DjangoModelPermissions]
    serializer_class = UserSerializer
    permission_classes = [IsOwner]
    # queryset = USER.objects.all()
    def get_queryset(self):
        queryset = User.objects.all()
        user = self.request.user
        print(user)
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(username=username)
        # User.objects.filter(username=user)
        return queryset
    
