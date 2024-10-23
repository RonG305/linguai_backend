from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserRoles(models.Model):

    name = models.CharField(max_length=50, unique=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user roles'


class AssignRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=200)

    class Meta:
        db_table = 'assign roles'