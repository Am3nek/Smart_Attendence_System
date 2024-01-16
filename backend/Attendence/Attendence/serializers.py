from rest_framework import serializers
from .models import StudentData

class SDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        fields = '__all__'
