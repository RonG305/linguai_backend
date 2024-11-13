from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from accounts.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login as django_login, authenticate, logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.models import AssignRole


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):  # Make sure this is the correct name
    print("Received request data:", request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def signin_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(request, username=username, password=password)

    
    if user is not None:
        django_login(request, user)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        userId = request.user.id
        print("userId", userId)

        try:
            user_role = AssignRole.objects.get(user=request.user).role
           
        except AssignRole.DoesNotExist:
            user_role = 'user'

        return Response({'message': 'Login successful', 'access_token': access_token,  'role': user_role , 'username': username, "userId": userId}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    logout(request)
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)  