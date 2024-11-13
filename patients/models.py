from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
   
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    national_id =models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField()
    email = models.EmailField()
    diagnoses = models.TextField()
    county = models.CharField(max_length=250, null=True, blank=True)
    subcounty = models.CharField(max_length=250, null=True, blank=True)
    ward = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self) -> str:
        return self.full_name


