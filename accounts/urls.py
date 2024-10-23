from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.signin_user, name='signup'),
    path('signin/', views.signin_user, name='signin')
]