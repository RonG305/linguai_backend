from django.db import models

# Create your models here.
class Patient(models.Model):
   
    id = models.AutoField(primary_key=True)
    national_id =models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField()
    email = models.EmailField()
    diagnoses = models.TextField()

    def __str__(self) -> str:
        return self.full_name


