from django.shortcuts import render
import json
from django.http import JsonResponse
import numpy as np
import pandas as pd
from diagnosis.models import Diagnosis
from patients.models import Patient
from .ai_model import get_predicted_value, helper
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def predict_disease(request):
    try:
        data = request.data

        # Check for symptoms in the data
        symptoms = data.get('symptoms')
        patient_id = data.get('patient_id')

        if not symptoms or not patient_id:
            return JsonResponse({
                "message": "Please either write symptoms or you have written misspelled symptoms",
                "status": "error"
            }, status=400)

        # Get the patient by ID
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return JsonResponse({
                "message": "Patient not found",
                "status": "error"
            }, status=404)

        # Process the symptoms
        user_symptoms = [s.strip() for s in symptoms.split(',')]
        user_symptoms = [symptom.strip("[]' ") for symptom in user_symptoms] 

       
        predicted_disease = get_predicted_value(user_symptoms)
        dis_des, precautions, medications, rec_diet, workout = helper(predicted_disease)
        precautions = list(precautions[0])

        if isinstance(precautions, pd.Series):
            precautions = precautions.tolist()
        if isinstance(dis_des, pd.Series):
            dis_des = dis_des.tolist()
        if isinstance(medications, pd.Series):
            medications = medications.tolist()
        if isinstance(rec_diet, pd.Series):
            rec_diet = rec_diet.tolist()
        if isinstance(workout, pd.Series):
            workout = workout.tolist()



        precautions = json.dumps(precautions) if isinstance(precautions, list) else precautions
        medications = json.dumps(medications) if isinstance(medications, list) else medications
        rec_diet = json.dumps(rec_diet) if isinstance(rec_diet, list) else rec_diet
        workout = json.dumps(workout) if isinstance(workout, list) else workout    

     
        new_diagnosis = Diagnosis(
            predicted_disease=predicted_disease,
            symptoms=symptoms,
            precautions=precautions,
            medications=medications,
            recommended_diet=rec_diet,
            workout=workout,
            patient_id=patient
        )
        new_diagnosis.save()

        # Return the prediction result
        return JsonResponse({
            'predicted_disease': predicted_disease,
            'disease_description': dis_des,
            'precautions': precautions,
            'medications': medications,
            'recommended_diet': rec_diet,
            'work_out': workout
        }, status=200)

    except Exception as e:
        return JsonResponse({
            'response': str(e),
            'status': 'error'
        }, status=500)
