from django.db import models
from patients.models import Patient

# Create your models here.
class Diagnosis(models.Model):
   
    id =models.AutoField(primary_key=True)
    predicted_disease = models.CharField(max_length=200)
    symptoms = models.TextField()
    precautions = models.TextField()
    medications = models.TextField()
    recommended_diet = models.TextField()
    workout = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f" Diagnosis for: {self.patient_id.full_name}"