from django.contrib import admin
from accounts.models import UserRoles, AssignRole

# Register your models here.
admin.site.register(UserRoles)
admin.site.register(AssignRole)