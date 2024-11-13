from django.urls import path
from diagnosis import views

urlpatterns = [
    path('diagnoses/all', views.get_diagnoses, name='diagnoses'),
    path('dignoses/data/patient/', views.get_patient_diagnoses, name='patient_diagnoses') ,
     
]