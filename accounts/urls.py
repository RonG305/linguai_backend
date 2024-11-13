from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('signin/', views.signin_user, name='signin') ,
    path('logout/', views.logout_user, name="logout")  
]