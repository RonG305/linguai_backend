from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
                                     'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={
                                      'input_type': 'password'})


    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password", "password2"]

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("the two passords dont match")
        return data 
    
    def create(self, validated_data):
        password = validated_data.pop("password")
       
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data, password=password)
       

        return user