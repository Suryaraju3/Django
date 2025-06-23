# from django.shortcuts import render

from rest_framework import generics
from .models import Doctors,Patient,Prescription,Payment
from .serializes import DoctorsSerializer,PatientSerializer,PrescriptionSerializer,PaymentSerializer

class  DoctorsList(generics.ListCreateAPIView):
    queryset = Doctors
    serializer_class = DoctorsSerializer

class PatientList(generics.ListCreateAPIView):
    queryset = Doctors
    serializer_class = PatientSerializer

class PerscriptionList(generics.ListCreateAPIView):
    queryset = Prescription
    serializer_class = PrescriptionSerializer
class PaymentList(generics.ListCreateAPIView):
    queryset = Payment
    serializer_class = PaymentSerializer
     