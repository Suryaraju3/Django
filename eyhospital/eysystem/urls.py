from django.urls import path
from .views import DoctorsList,PatientList,PerscriptionList,PaymentList

urlpatterns = [
     path('ey/',DoctorsList.as_view(),name='ey-system'),
     path('Patient/',PatientList.as_view(),name='ey-system'),
     path('Perscription/',PerscriptionList.as_view(),name='ey-system'),
     path('Pay/',PaymentList.as_view(),name="ey-system")
     
     
 ]
 