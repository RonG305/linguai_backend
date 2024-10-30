from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from patients.serializers import PatientSerializer
from patients.models import Patient

# Create your views here.

@api_view(['GET'])
def get_patients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_patient(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_patient(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response({"message": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = PatientSerializer(patient)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_patient(request):
    data = request.data
    national_id = data.get('national_id')
    full_name = data.get('full_name')
    age = data.get('age')
    email = data.get('email')
    diagnoses = data.get('diagnoses')
    county = data.get('county')
    subcounty = data.get('subcounty')
    ward = data.get('ward')

    new_patient = Patient(
        national_id=national_id,
        full_name=full_name,
        age=age,
        email=email,
        diagnoses=diagnoses,
        county=county,
        subcounty=subcounty,
        ward=ward
    )

    new_patient.save()
    serializer = PatientSerializer(new_patient)
    return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_patient(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response({"message": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = PatientSerializer(patient, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

@api_view(['DELETE'])
def delete_patient(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response({"message": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
    
    patient.delete()
    return Response({'response': "Patient deleted succesifully"}, status=status.HTTP_204_NO_CONTENT)

