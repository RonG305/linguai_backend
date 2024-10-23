from django.urls import path
from prediction_model import views

urlpatterns = [
    path('predict/', views.predict_disease, name='predict')
]