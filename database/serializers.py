from rest_framework import serializers
from .models import Clase, SubjectsPrimary1,SubjectsPrimary2,USER

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'
class SubjectsPrimary1Serializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectsPrimary1
        fields = '__all__'
class SubjectsPrimary2Serializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectsPrimary2
        fields = '__all__'
class USERSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER
        fields = '__all__'

