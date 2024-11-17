from rest_framework import serializers
from .models import StudentProfile, TPOProfile, CompanyProfile

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'

class TPOProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPOProfile
        fields = '__all__'
        
class CompanyProileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = '__all__'