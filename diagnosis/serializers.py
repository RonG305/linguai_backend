from diagnosis.models import Diagnosis
from rest_framework import serializers

class DiagnosisSerializer(serializers.ModelSerializer):
   class Meta:
      model = Diagnosis
      fields = ['id', 'predicted_disease', 'symptoms', 'precautions', 'medications', 'recommended_diet', 'workout', 'timestamp', 'patient_id']