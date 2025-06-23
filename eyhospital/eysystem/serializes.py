from rest_framework import serializers
from .models import Doctors,Patient,Prescription,Payment

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields='__all__' 
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        