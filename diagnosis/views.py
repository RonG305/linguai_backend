from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from diagnosis.serializers import DiagnosisSerializer
from patients.models import Patient
from diagnosis.models import Diagnosis
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
# @api_view(['GET'])
# def get_diagnoses(request):
#     diagnoses = Diagnosis.objects.all()
#     serializer = DiagnosisSerializer(diagnoses, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_diagnoses(request):
    diagnoses = Diagnosis.objects.all()
    serializer = DiagnosisSerializer(diagnoses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_patient_diagnoses(request):
    try:
        patient = Patient.objects.get(user=request.user)
        print(request.user)  # Get the Patient instance
        diagnoses = Diagnosis.objects.filter(patient_id=patient)
        print(diagnoses)  # Filter diagnoses for that patient
        serializer = DiagnosisSerializer(diagnoses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Patient.DoesNotExist:
        return Response({'error': 'Patient not found for the logged-in user'}, status=status.HTTP_404_NOT_FOUND)
