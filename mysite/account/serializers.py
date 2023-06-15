from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  CustomUser
        fields = ['url', 'username', 'email', 'first_name', 'last_name', 'is_staff']


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']


    def validate(self, data, request=None):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials')



class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'last_name', 'first_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, data):
        data = {key: data[key] for key in ['username', 'last_name', 'first_name', 'email', 'password']}
        user = CustomUser.objects.create(**data)
        return user