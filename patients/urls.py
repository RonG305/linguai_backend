from django.urls import path
from patients import views

urlpatterns = [
    path('get_patients', views.get_patients, name='get_patients'),
    path('create_patient', views.create_patient, name='create_patient'),
    path('patient/<int:pk>/get_patient', views.get_patient, name='get_patient'),
    path('patient/<int:pk>/update_patient/', views.update_patient, name='update_patient'),
    path('patient/<int:pk>/delete_patient', views.delete_patient, name='delete_patient'),
]